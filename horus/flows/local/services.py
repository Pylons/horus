from ..exceptions import (
    AuthenticationException,
    UserExistsException
)


class UserService(object):
    """
    UserFacade is used to manage all the business logic for
    authentication and registration of users. It uses an
    `IUserService` class to interface with the persistence layer.
    """
    def __init__(self, backend):
        self.service = service

    def authenticate(self, username, password):
        """
        Retrieves a user from the data store and verifies
        the password matches.
        """
        #TODO: Check if the user is activated?
        user = self.service.get_user(username)

        if (
            user is None or
            user.password != password
        ):
            raise AuthenticationException()

        return user

    def register(self, username, password, email=None):
        """
        Will create a user in the database
        """
        user = self.service.get_user(username)

        if user is not None:
            raise UserExistsException()

        user = self.service.create_user(
            username,
            password,
            email
        )

        return user
