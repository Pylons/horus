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
        from horus.facades.user import UserFacade

        def get_user(login):
            if login == 'sontek':
                return self._make_user(login, 'drowssap')
            else:
                return None

        s = mock.Mock()
        s.get_user = get_user
        f = UserFacade(s)

        result = f.authenticate('sontek', 'drowssap')

        assert result is not None

    @pytest.mark.unit
    def test_authenticate_bad_user(self):
        from horus.facades.user import UserFacade
        from horus.exceptions import AuthenticationException

        def get_user(login):
            if login == 'sontek':
                return self._make_user(login, 'drowssap')
            else:
                return None

        s = mock.Mock()
        s.get_user = get_user
        f = UserFacade(s)

        with pytest.raises(AuthenticationException):
            f.authenticate('fred', 'drowssap')

    @pytest.mark.unit
    def test_authenticate_bad_password(self):
        from horus.facades.user import UserFacade
        from horus.exceptions import AuthenticationException

        user = self._make_user('sontek', 'drowssap')
        s = mock.Mock()
        s.get_user.return_value = user

        f = UserFacade(s)

        with pytest.raises(AuthenticationException):
            f.authenticate('fred', 'drowssap1')

    @pytest.mark.unit
    def test_authenticate_register_user(self):
        from horus.facades.user import UserFacade

        s = mock.Mock()
        s.get_user.return_value = None
        s.create_user.return_value = self._make_user
        f = UserFacade(s)

        user = f.register('fred', 'drowssap1')
        assert user is not None

    @pytest.mark.unit
    def test_authenticate_register_user_already_exists(self):
        from horus.facades.user import UserFacade
        from horus.exceptions import UserExistsException

        s = mock.Mock()
        user = self._make_user('sontek', 'drowssap')
        s.get_user.return_value = None
        s.create_user.return_value = self._make_user
        s.get_user.return_value = user

        f = UserFacade(s)

        with pytest.raises(UserExistsException):
            f.register('fred', 'drowssap1')

