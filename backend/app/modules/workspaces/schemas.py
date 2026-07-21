import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class WorkspaceBase(BaseModel):
    name: str
    slug: str
    description: str | None = None


class WorkspaceCreate(WorkspaceBase):
    pass


class WorkspaceRead(WorkspaceBase):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    owner_id: uuid.UUID
    is_active: bool
    created_at: datetime
