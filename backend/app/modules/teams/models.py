from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base
from app.core.mixins import ActiveMixin, TimestampMixin, UUIDMixin


class Team(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "teams"
    __table_args__ = {"schema": "teams"}

    enterprise_id = Column(UUID(as_uuid=True), ForeignKey("enterprises.enterprises.id", ondelete="CASCADE"), nullable=True, index=True)
    name = Column(String(150), nullable=False)
    description = Column(String(1000), nullable=True)
