import uuid

from pydantic import BaseModel, ConfigDict

from app.modules.billing.models import SubscriptionStatus


class SubscriptionCreate(BaseModel):
    workspace_id: uuid.UUID
    plan_name: str = "FREE"


class SubscriptionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    workspace_id: uuid.UUID
    plan_name: str
    status: SubscriptionStatus
