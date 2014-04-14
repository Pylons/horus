from ..exceptions import AuthenticationFailure


class UserFacade(object):
    """
    UserFacade is used to manage all the business logic for
    authentication and registration of users. It uses an
    `IUserService` class to interface with the persistence layer.
    """
    def __init__(self, service):
        self.service = service

    def authenticate_user(self, username, password):
        user = self.service.get_user(username)

        if (
            user is None or
            user.password != password
        ):
            raise AuthenticationFailure()

        return user
