import uuid

from pydantic import BaseModel, ConfigDict

from app.modules.inference.models import InferenceStatus


class InferenceRequestCreate(BaseModel):
    deployment_id: uuid.UUID
    input_data: dict = {}


class InferenceRequestRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    deployment_id: uuid.UUID
    input_data: dict
    output_data: dict
    status: InferenceStatus
