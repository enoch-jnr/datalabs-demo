import uuid

from pydantic import BaseModel, ConfigDict


class ApiKeyCreate(BaseModel):
    name: str
    scopes: list[str] = []


class ApiKeyRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    user_id: uuid.UUID
    name: str
    key_prefix: str
    scopes: list
    is_active: bool
