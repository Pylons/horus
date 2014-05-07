import pytest

from sqlalchemy.ext.declarative import declarative_base
from horus.backends.sqla.mixins import UserMixin

BaseModel = declarative_base()


class UserModel(UserMixin, BaseModel):
    pass


@pytest.mark.sqla
def test_user_class(db_session):

    user = UserModel(username='sontek')
    db_session.add(user)
    db_session.flush()
    results = db_session.query(UserModel).all()
    assert results[0] == user


@pytest.mark.sqla
def test_user_class_hashes_password(db_session):
    user = UserModel(username=u'tilgovi', password=u'seekrit')
    assert user.password != u'seekrit'
