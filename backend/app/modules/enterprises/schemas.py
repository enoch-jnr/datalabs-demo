import uuid

from pydantic import BaseModel, ConfigDict


class EnterpriseCreate(BaseModel):
    name: str
    code: str
    industry: str | None = None


class EnterpriseRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    code: str
    industry: str | None
    is_active: bool
