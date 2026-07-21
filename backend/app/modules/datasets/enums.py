from enum import Enum


class DatasetStatus(str, Enum):
    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"


class DatasetVisibility(str, Enum):
    PRIVATE = "PRIVATE"
    PROJECT = "PROJECT"
    PUBLIC = "PUBLIC"


class DatasetSplit(str, Enum):
    TRAIN = "TRAIN"
    VALIDATION = "VALIDATION"
    TEST = "TEST"
    UNASSIGNED = "UNASSIGNED"
