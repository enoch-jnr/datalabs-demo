import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.modules.notifications.enums import NotificationType


class NotificationRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    notification_type: NotificationType
    title: str
    body: str | None
    link_url: str | None
    is_read: bool
    created_at: datetime


class NotificationPreferenceUpdate(BaseModel):
    email_enabled: bool | None = None
    sms_enabled: bool | None = None
    in_app_enabled: bool | None = None


class NotificationPreferenceRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    email_enabled: bool
    sms_enabled: bool
    in_app_enabled: bool
