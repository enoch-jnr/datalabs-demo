import uuid

from pydantic import BaseModel, ConfigDict


class TeamCreate(BaseModel):
    enterprise_id: uuid.UUID | None = None
    name: str
    description: str | None = None


class TeamRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    enterprise_id: uuid.UUID | None
    name: str
    description: str | None
    is_active: bool
