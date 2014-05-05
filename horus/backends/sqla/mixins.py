from bcrypt import gensalt, hashpw
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.hybrid import hybrid_property
from horus.interfaces import IUser
from zope.interface import implements
import sqlalchemy as sa


class BaseMixin(object):
    @declared_attr
    def id(self):
        return sa.Column(sa.Integer, autoincrement=True, primary_key=True)


class UserMixin(BaseMixin):
    implements(IUser)

    __tablename__ = 'user'

    @declared_attr
    def username(self):
        """ Unique username """
        return sa.Column(sa.Unicode(30), nullable=False, unique=True)

    @declared_attr
    def date_registered(self):
        """ Date of user's registration """
        return sa.Column(
            sa.TIMESTAMP(timezone=False),
            default=sa.sql.func.now(),
            server_default=sa.func.now(),
            nullable=False,
        )

    @declared_attr
    def salt(self):
        """ Password salt for user """
        return sa.Column(sa.Binary(29), nullable=True)

    @declared_attr
    def _password(self):
        """ Password hash for user object """
        return sa.Column('password', sa.Binary(60), nullable=True)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._set_password(value)

    def _get_password(self):
        return self._password

    def _set_password(self, raw_password):
        self._password = self._hash_password(raw_password)

    def _hash_password(self, password):
        if self.salt is None:
            self.salt = gensalt(12)

        return unicode(hashpw(password.encode('utf-8'), self.salt))
