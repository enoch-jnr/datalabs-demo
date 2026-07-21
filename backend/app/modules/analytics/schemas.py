import uuid

from pydantic import BaseModel, ConfigDict


class DashboardCreate(BaseModel):
    project_id: uuid.UUID
    name: str
    widgets_config: list = []


class DashboardRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    project_id: uuid.UUID
    name: str
    widgets_config: list
