from zope.interface import (
    Interface,
    Attribute
)


class IUser(Interface):
    login = Attribute('The value used to do authentication')
    password = Attribute('The password for verifying the user')


class ILoginService(Interface):
    pass


class IActivationService(Interface):
    pass


class IRegistrationService(Interface):
    pass


class IMailer(Interface):
    pass
