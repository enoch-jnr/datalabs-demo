import enum

from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base
from app.core.mixins import ActiveMixin, TimestampMixin, UUIDMixin


class MarketplaceItemType(str, enum.Enum):
    PLUGIN = "PLUGIN"
    DATASET = "DATASET"
    MODEL = "MODEL"


class MarketplaceItem(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "marketplace_items"
    __table_args__ = {"schema": "marketplace"}

    publisher_id = Column(UUID(as_uuid=True), ForeignKey("core.users.id", ondelete="SET NULL"), nullable=True, index=True)
    name = Column(String(150), nullable=False)
    item_type = Column(Enum(MarketplaceItemType), nullable=False)
    description = Column(String(2000), nullable=True)
    price_cents = Column(Integer, nullable=False, default=0)
