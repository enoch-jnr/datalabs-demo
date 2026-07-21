import uuid

from pydantic import BaseModel, ConfigDict

from app.modules.training.models import TrainingJobStatus


class TrainingJobCreate(BaseModel):
    project_id: uuid.UUID
    name: str
    configuration: dict = {}


class TrainingJobRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    project_id: uuid.UUID
    name: str
    status: TrainingJobStatus
