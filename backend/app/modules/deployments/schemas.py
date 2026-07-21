import uuid

from pydantic import BaseModel, ConfigDict

from app.modules.deployments.models import DeploymentStatus


class DeploymentCreate(BaseModel):
    project_id: uuid.UUID
    model_id: uuid.UUID | None = None
    name: str


class DeploymentRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    project_id: uuid.UUID
    model_id: uuid.UUID | None
    name: str
    endpoint_url: str | None
    status: DeploymentStatus
