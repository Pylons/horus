class AuthenticationFailure(Exception):
    """
    Exception that represents when authentication was
    attempted and the user did not exist or the password
    was invalid
    """
    pass
