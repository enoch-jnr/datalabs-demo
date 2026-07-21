from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.core.mixins import TimestampMixin, UUIDMixin
from app.modules.notifications.enums import NotificationType


class Notification(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "notifications"
    __table_args__ = {"schema": "notifications"}

    recipient_id = Column(UUID(as_uuid=True), ForeignKey("core.users.id", ondelete="CASCADE"), nullable=False, index=True)

    notification_type = Column(Enum(NotificationType), nullable=False)
    title = Column(String(200), nullable=False)
    body = Column(String(2000), nullable=True)
    link_url = Column(String(500), nullable=True)
    data = Column(JSONB, nullable=False, default=dict)

    is_read = Column(Boolean, nullable=False, default=False, index=True)
    read_at = Column(DateTime(timezone=True), nullable=True)

    recipient = relationship("User", foreign_keys="Notification.recipient_id")


class NotificationPreference(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "notification_preferences"
    __table_args__ = {"schema": "notifications"}

    user_id = Column(UUID(as_uuid=True), ForeignKey("core.users.id", ondelete="CASCADE"), nullable=False, unique=True, index=True)
    email_enabled = Column(Boolean, nullable=False, default=True)
    sms_enabled = Column(Boolean, nullable=False, default=False)
    in_app_enabled = Column(Boolean, nullable=False, default=True)

    user = relationship("User", foreign_keys="NotificationPreference.user_id")
