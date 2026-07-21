import uuid

from pydantic import BaseModel, ConfigDict

from app.modules.pipelines.models import PipelineStatus


class PipelineCreate(BaseModel):
    project_id: uuid.UUID
    name: str
    definition: dict = {}


class PipelineRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    project_id: uuid.UUID
    name: str
    status: PipelineStatus
