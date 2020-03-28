import pytest
import os
import mock

from pyramid.paster import get_appsettings
from pyramid import testing
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker

here = os.path.dirname(__file__)
config_file = os.path.join(here, 'test.ini')
settings = get_appsettings(config_file)
_DBSession = None
_DBTrans = None
current_session = None


class NotAllowed(Exception):
    message = 'You must mark your test as sqla'


def pytest_addoption(parser):
    parser.addoption(
        "--slow",
        action="store_true",
        help="run slow tests"
    )

    parser.addoption(
        "--sqla",
        action="store_true",
        help="run sqla tests"
    )


def setup_sqlalchemy():
        global DBTrans
        global _DBSession

        testing.setUp(settings=settings)

        engine = engine_from_config(settings, prefix='backend.sqla.')
        connection = engine.connect()
        DBTrans = connection.begin()
        _DBSession = sessionmaker(bind=connection)()


def pytest_runtest_setup(item):
    global current_session
    current_session = None

    if 'slow' in item.keywords and not item.config.getoption("--slow"):
        pytest.skip("need --slow option to run")
        return

    if 'sqla' in item.keywords and not item.config.getoption("--sqla"):
        pytest.skip("need --sqla option to run")
        return
    else:
        current_session = _DBSession


@pytest.fixture()
def db_session(request):
    """
    This will handle the db session to tests that declare session in
    their arguments
    """
    if 'sqla' in request.keywords:
        return current_session
    else:
        raise NotAllowed('This test is not a sqla test')


def pytest_sessionstart():
    from py.test import config

    is_sqla = config.getoption('--sqla')

    # Only run database setup on master (in case of xdist/multiproc mode)
    if not hasattr(config, 'slaveinput') and is_sqla:
        from pyramid.config import Configurator
        from .backends.test_sql import BaseModel
        setup_sqlalchemy()
        engine = _DBSession.bind.engine
        print('Creating the tables on the test database %s' % engine)
        config = Configurator(settings=settings)
        BaseModel.metadata.bind = _DBSession.bind
        BaseModel.metadata.drop_all(engine)
        BaseModel.metadata.create_all(engine)
