import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.audit.models import AuditLog


async def log_action(
    db: AsyncSession,
    action: str,
    resource_type: str,
    actor_id: uuid.UUID | None = None,
    resource_id: uuid.UUID | None = None,
    details: dict | None = None,
) -> AuditLog:
    """
    Fire-and-forget style audit write. Call this from any module's
    service layer after a meaningful action (create/update/delete,
    login, review decision, etc.) so everything lands in one place
    instead of a per-module audit table.
    """
    entry = AuditLog(
        actor_id=actor_id,
        action=action,
        resource_type=resource_type,
        resource_id=resource_id,
        details=details or {},
    )
    db.add(entry)
    await db.commit()
    return entry
