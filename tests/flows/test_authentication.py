import pytest
import mock
from horus.interfaces import IUser
from zope.interface import implements


class UserImpl(object):
    implements(IUser)

    def __init__(self, login, password, emails=None):
        self.login = login
        self.password = password
        self.emails = emails


class TestUserFacade(object):
    def _make_user(self, login, password, email=None):
        emails = None

        if email is not None:
            emails = [email]

        return UserImpl(login, password, emails)

    @pytest.mark.unit
    def test_authenticate_good_user(self):
        from horus.flows.local.services import AuthenticationService

        def get_user(login):
            if login == 'sontek':
                return self._make_user(login, 'drowssap')
            else:
                return None

        s = mock.Mock()
        s.get_user = get_user
        f = AuthenticationService(s)

        result = f.login('sontek', 'drowssap')

        assert result is not None

    @pytest.mark.unit
    def test_authenticate_bad_user(self):
        from horus.flows.local.services import AuthenticationService
        from horus.exceptions import AuthenticationException

        def get_user(login):
            if login == 'sontek':
                return self._make_user(login, 'drowssap')
            else:
                return None

        s = mock.Mock()
        s.get_user = get_user
        f = AuthenticationService(s)

        with pytest.raises(AuthenticationException):
            f.login('fred', 'drowssap')

    @pytest.mark.unit
    def test_authenticate_bad_password(self):
        from horus.flows.local.services import AuthenticationService
        from horus.exceptions import AuthenticationException

        user = self._make_user('sontek', 'drowssap')
        s = mock.Mock()
        s.get_user.return_value = user

        f = AuthenticationService(s)

        with pytest.raises(AuthenticationException):
            f.login('fred', 'drowssap1')

    @pytest.mark.unit
    def test_authenticate_register_user(self):
        from horus.flows.local.services import RegisterService

        s = mock.Mock()
        s.get_user.return_value = None
        s.create_user.return_value = self._make_user
        f = RegisterService(s)

        user = f.create_user('fred', 'drowssap1')
        assert user is not None

    @pytest.mark.unit
    def test_authenticate_register_user_already_exists(self):
        from horus.flows.local.services import RegisterService
        from horus.exceptions import UserExistsException

        s = mock.Mock()
        user = self._make_user('sontek', 'drowssap')
        s.get_user.return_value = None
        s.create_user.return_value = self._make_user
        s.get_user.return_value = user

        f = RegisterService(s)

        with pytest.raises(UserExistsException):
            f.create_user('fred', 'drowssap1')

