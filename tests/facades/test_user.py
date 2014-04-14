import pytest
import mock
from horus.interfaces import IUser
from zope.interface import implements


class UserImpl(object):
    implements(IUser)

    def __init__(self, login):
        self.login = login


class TestUserFacade(object):
    def _makeUser(self, login):
        return UserImpl(login)

    @pytest.mark.unit
    def test_authenticate_good_user(self):
        from horus.facades.user import UserFacade

        def get_user(login):
            if login == 'sontek':
                return self._makeUser(login)
            else:
                return None

        s = mock.Mock()
        s.get_user = get_user
        f = UserFacade(s)

        result = f.authenticate_user('sontek', 'drowssap')

        assert result is not None

    @pytest.mark.unit
    def test_authenticate_bad_user(self):
        from horus.facades.user import UserFacade
        from horus.exceptions import AuthenticationFailure

        def get_user(login):
            if login == 'sontek':
                return self._makeUser(login)
            else:
                return None

        s = mock.Mock()
        s.get_user = get_user
        f = UserFacade(s)

        with pytest.raises(AuthenticationFailure):
            f.authenticate_user('fred', 'drowssap')

