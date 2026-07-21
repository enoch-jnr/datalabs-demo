import enum

from sqlalchemy import Column, Enum, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base
from app.core.mixins import ActiveMixin, TimestampMixin, UUIDMixin


class SubscriptionStatus(str, enum.Enum):
    TRIALING = "TRIALING"
    ACTIVE = "ACTIVE"
    PAST_DUE = "PAST_DUE"
    CANCELED = "CANCELED"


class Subscription(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "subscriptions"
    __table_args__ = {"schema": "billing"}

    workspace_id = Column(UUID(as_uuid=True), ForeignKey("workspaces.workspaces.id", ondelete="CASCADE"), nullable=False, index=True)
    plan_name = Column(String(100), nullable=False, default="FREE")
    status = Column(Enum(SubscriptionStatus), nullable=False, default=SubscriptionStatus.TRIALING)
