from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB, UUID

from app.core.database import Base
from app.core.mixins import TimestampMixin, UUIDMixin


class AuditLog(Base, UUIDMixin, TimestampMixin):
    """
    Central audit log — every module can write here instead of keeping
    its own per-module audit table, per the 'central audit service'
    goal from the architecture doc.
    """

    __tablename__ = "audit_logs"
    __table_args__ = {"schema": "audit"}

    actor_id = Column(UUID(as_uuid=True), ForeignKey("core.users.id", ondelete="SET NULL"), nullable=True, index=True)
    action = Column(String(100), nullable=False, index=True)
    resource_type = Column(String(100), nullable=False, index=True)
    resource_id = Column(UUID(as_uuid=True), nullable=True, index=True)
    ip_address = Column(String(50), nullable=True)
    details = Column(JSONB, nullable=False, default=dict)
