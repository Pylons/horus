from zope.interface import (
    Interface,
    Attribute
)


class IUser(Interface):
    login = Attribute('The value used to do authentication')
    password = Attribute('The password for verifying the user')
    date_registered = Attribute('')
    salt = Attribute('')


class ILoginService(Interface):
    pass


class IActivationService(Interface):
    pass


class IRegistrationService(Interface):
    pass


class IMailer(Interface):
    pass


class IDataBackend(Interface):
    def get_user(self, login):
        pass

    def create_user(self, login, password=None, email=None):
        pass
