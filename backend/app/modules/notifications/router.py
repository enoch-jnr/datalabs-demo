import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import get_current_active_user
from app.modules.core.models import User
from app.modules.notifications import service
from app.modules.notifications.schemas import (
    NotificationPreferenceRead,
    NotificationPreferenceUpdate,
    NotificationRead,
)

router = APIRouter(prefix="/notifications", tags=["notifications"])


@router.get("/", response_model=list[NotificationRead])
async def list_notifications(
    unread_only: bool = False,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    return await service.list_notifications(db, current_user.id, unread_only)


@router.post("/{notification_id}/read", response_model=NotificationRead)
async def mark_read(
    notification_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    return await service.mark_read(db, current_user.id, notification_id)


@router.get("/preferences", response_model=NotificationPreferenceRead)
async def get_preferences(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    return await service.get_or_create_preferences(db, current_user.id)


@router.patch("/preferences", response_model=NotificationPreferenceRead)
async def update_preferences(
    payload: NotificationPreferenceUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    return await service.update_preferences(db, current_user.id, payload.model_dump())
