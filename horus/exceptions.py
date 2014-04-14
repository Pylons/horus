class AuthenticationException(Exception):
    """
    Exception that represents when authentication was
    attempted and the user did not exist or the password
    was invalid
    """
    pass


class UserExistsException(Exception):
    """
    Exception that represents when registration was
    attempted and the user or email is already taken
    """
    pass
