from sqlalchemy.ext.declarative import declared_attr

class BaseMixin(object):
    pass

class UserMixin(object):
    @declared_attr
    def principals(self):
        pass

class UserGroupLinkMixin(object):
    pass

class GroupMixin(object):
    pass

class UserRoleLinkMixin(object):
    pass

class RoleMixin(object):
    pass
