import pytest
import mock
from horus.interfaces import IUser
from zope.interface import implements


class UserImpl(object):
    implements(IUser)

    def __init__(self, login, password):
        self.login = login
        self.password = password


class TestUserFacade(object):
    def _make_user(self, login, password):
        return UserImpl(login, password)

    @pytest.mark.unit
    def test_authenticate_good_user(self):
        from horus.facades.user import UserFacade

        def get_user(login):
            if login == 'sontek':
                return self._make_user(login, 'drowssap')
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
                return self._make_user(login, 'drowssap')
            else:
                return None

        s = mock.Mock()
        s.get_user = get_user
        f = UserFacade(s)

        with pytest.raises(AuthenticationFailure):
            f.authenticate_user('fred', 'drowssap')

    @pytest.mark.unit
    def test_authenticate_bad_password(self):
        from horus.facades.user import UserFacade
        from horus.exceptions import AuthenticationFailure

        user = self._make_user('sontek', 'drowssap')
        s = mock.Mock()
        s.get_user.return_value = user

        f = UserFacade(s)

        with pytest.raises(AuthenticationFailure):
            f.authenticate_user('fred', 'drowssap1')

