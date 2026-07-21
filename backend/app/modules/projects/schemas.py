import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.modules.projects.enums import ProjectStatus, ProjectVisibility


class ProjectBase(BaseModel):
    name: str
    code: str
    description: str | None = None
    visibility: ProjectVisibility = ProjectVisibility.PRIVATE


class ProjectCreate(ProjectBase):
    workspace_id: uuid.UUID


class ProjectUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    visibility: ProjectVisibility | None = None
    status: ProjectStatus | None = None


class ProjectRead(ProjectBase):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    workspace_id: uuid.UUID
    status: ProjectStatus
    is_active: bool
    created_at: datetime
