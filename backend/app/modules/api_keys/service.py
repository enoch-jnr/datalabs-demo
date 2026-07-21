import secrets
import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import hash_password
from app.modules.api_keys.models import ApiKey


async def create_api_key(db: AsyncSession, user_id: uuid.UUID, name: str, scopes: list[str]) -> tuple[ApiKey, str]:
    """Returns (record, raw_key) — the raw key is only ever shown once."""
    raw_key = f"dl_{secrets.token_urlsafe(32)}"
    record = ApiKey(
        user_id=user_id,
        name=name,
        key_prefix=raw_key[:10],
        hashed_key=hash_password(raw_key),
        scopes=scopes,
    )
    db.add(record)
    await db.commit()
    await db.refresh(record)
    return record, raw_key
