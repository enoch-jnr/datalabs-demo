import uuid

from pydantic import BaseModel, ConfigDict


class PluginCreate(BaseModel):
    name: str
    version: str = "0.1.0"
    description: str | None = None


class PluginRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    version: str
    description: str | None
    is_active: bool
