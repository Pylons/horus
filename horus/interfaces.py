from zope.interface import (
    Interface,
    Attribute
)


class IUser(Interface):
    login = Attribute('The value used to do authentication')
