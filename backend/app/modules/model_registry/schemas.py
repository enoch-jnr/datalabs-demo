import uuid

from pydantic import BaseModel, ConfigDict

from app.modules.model_registry.models import ModelStage


class MLModelCreate(BaseModel):
    project_id: uuid.UUID
    name: str
    description: str | None = None


class MLModelRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    project_id: uuid.UUID
    name: str
    description: str | None
    stage: ModelStage
