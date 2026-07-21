from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB, UUID

from app.core.database import Base
from app.core.mixins import ActiveMixin, TimestampMixin, UUIDMixin


class ApiKey(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "api_keys"
    __table_args__ = {"schema": "api_keys"}

    user_id = Column(UUID(as_uuid=True), ForeignKey("core.users.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(150), nullable=False)
    key_prefix = Column(String(20), nullable=False)
    hashed_key = Column(String(255), nullable=False)
    scopes = Column(JSONB, nullable=False, default=list)
