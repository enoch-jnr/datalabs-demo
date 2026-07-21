from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import get_current_active_user
from app.modules.api_keys import service
from app.modules.api_keys.models import ApiKey
from app.modules.api_keys.schemas import ApiKeyCreate, ApiKeyRead
from app.modules.core.models import User

router = APIRouter(prefix="/api-keys", tags=["api-keys"])


@router.post("/", status_code=201)
async def create_key(
    payload: ApiKeyCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    record, raw_key = await service.create_api_key(db, current_user.id, payload.name, payload.scopes)
    return {"api_key": ApiKeyRead.model_validate(record), "secret": raw_key}


@router.get("/", response_model=list[ApiKeyRead])
async def list_keys(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    result = await db.execute(select(ApiKey).where(ApiKey.user_id == current_user.id))
    return result.scalars().all()
