import uuid

from pydantic import BaseModel, ConfigDict


class StorageBucketCreate(BaseModel):
    project_id: uuid.UUID
    name: str
    provider: str = "LOCAL"
    quota_bytes: int = 0


class StorageBucketRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    project_id: uuid.UUID
    name: str
    provider: str
    quota_bytes: int
    used_bytes: int
