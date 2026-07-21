import uuid
from datetime import datetime, timezone

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.notifications.models import Notification, NotificationPreference


async def list_notifications(db: AsyncSession, user_id: uuid.UUID, unread_only: bool = False) -> list[Notification]:
    query = select(Notification).where(Notification.recipient_id == user_id)
    if unread_only:
        query = query.where(Notification.is_read.is_(False))
    result = await db.execute(query.order_by(Notification.created_at.desc()))
    return list(result.scalars().all())


async def mark_read(db: AsyncSession, user_id: uuid.UUID, notification_id: uuid.UUID) -> Notification:
    result = await db.execute(select(Notification).where(Notification.id == notification_id))
    notification = result.scalar_one_or_none()
    if notification is None or notification.recipient_id != user_id:
        raise HTTPException(status_code=404, detail="Notification not found")
    notification.is_read = True
    notification.read_at = datetime.now(timezone.utc)
    await db.commit()
    await db.refresh(notification)
    return notification


async def get_or_create_preferences(db: AsyncSession, user_id: uuid.UUID) -> NotificationPreference:
    result = await db.execute(select(NotificationPreference).where(NotificationPreference.user_id == user_id))
    prefs = result.scalar_one_or_none()
    if prefs is None:
        prefs = NotificationPreference(user_id=user_id)
        db.add(prefs)
        await db.commit()
        await db.refresh(prefs)
    return prefs


async def update_preferences(db: AsyncSession, user_id: uuid.UUID, updates: dict) -> NotificationPreference:
    prefs = await get_or_create_preferences(db, user_id)
    for field, value in updates.items():
        if value is not None:
            setattr(prefs, field, value)
    await db.commit()
    await db.refresh(prefs)
    return prefs
