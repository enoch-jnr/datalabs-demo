import uuid

from pydantic import BaseModel, ConfigDict

from app.modules.marketplace.models import MarketplaceItemType


class MarketplaceItemCreate(BaseModel):
    name: str
    item_type: MarketplaceItemType
    description: str | None = None
    price_cents: int = 0


class MarketplaceItemRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    publisher_id: uuid.UUID | None
    name: str
    item_type: MarketplaceItemType
    description: str | None
    price_cents: int
