import uuid

from pydantic import BaseModel, ConfigDict

from app.modules.registry.models import RegistryStage


class RegistryEntryCreate(BaseModel):
    name: str
    version: int = 1


class RegistryEntryRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    version: int
    stage: RegistryStage
