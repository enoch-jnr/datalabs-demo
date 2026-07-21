from enum import Enum


class ProjectVisibility(str, Enum):
    PRIVATE = "PRIVATE"
    WORKSPACE = "WORKSPACE"
    PUBLIC = "PUBLIC"


class ProjectStatus(str, Enum):
    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
