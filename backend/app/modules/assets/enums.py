from enum import Enum


class AssetType(str, Enum):
    IMAGE = "IMAGE"
    AUDIO = "AUDIO"
    VIDEO = "VIDEO"
    TEXT = "TEXT"
    DOCUMENT = "DOCUMENT"
    OTHER = "OTHER"


class AssetStatus(str, Enum):
    UPLOADING = "UPLOADING"
    READY = "READY"
    FAILED = "FAILED"
