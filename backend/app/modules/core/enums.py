from enum import Enum


class RoleScope(str, Enum):
    GLOBAL = "GLOBAL"
    ENTERPRISE = "ENTERPRISE"
    TEAM = "TEAM"
    WORKSPACE = "WORKSPACE"
    PROJECT = "PROJECT"


class PermissionAction(str, Enum):
    CREATE = "CREATE"
    READ = "READ"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    MANAGE = "MANAGE"
