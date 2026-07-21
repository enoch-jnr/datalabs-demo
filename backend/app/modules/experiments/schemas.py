import uuid

from pydantic import BaseModel, ConfigDict

from app.modules.experiments.models import ExperimentStatus


class ExperimentCreate(BaseModel):
    project_id: uuid.UUID
    name: str
    parameters: dict = {}


class ExperimentRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    project_id: uuid.UUID
    name: str
    status: ExperimentStatus
    metrics: dict
    parameters: dict
