import pytest
import mock


@pytest.mark.unit
def test_authenticate_good_user():
    from horus.facades.user import UserFacade
    from horus.models import User

    def get_user(username):
        if username == 'sontek':
            return User(username)
        else:
            return None

    s = mock.Mock()
    s.get_user = get_user
    f = UserFacade(s)

    result = f.authenticate_user('sontek', 'drowssap')

    assert result is not None


@pytest.mark.unit
def test_authenticate_bad_user():
    from horus.facades.user import UserFacade
    from horus.models import User
    from horus.exceptions import AuthenticationFailure

    def get_user(username):
        if username == 'sontek':
            return User(username)
        else:
            return None

    s = mock.Mock()
    s.get_user = get_user
    f = UserFacade(s)

    with pytest.raises(AuthenticationFailure):
        f.authenticate_user('fred', 'drowssap')
