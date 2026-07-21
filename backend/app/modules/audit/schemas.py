import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class AuditLogCreate(BaseModel):
    action: str
    resource_type: str
    resource_id: uuid.UUID | None = None
    details: dict = {}


class AuditLogRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    actor_id: uuid.UUID | None
    action: str
    resource_type: str
    resource_id: uuid.UUID | None
    details: dict
    created_at: datetime
