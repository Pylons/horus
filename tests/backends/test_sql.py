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
