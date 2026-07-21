import uuid

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import get_current_active_user
from app.modules.assets.enums import AssetStatus
from app.modules.assets.models import Asset
from app.modules.assets.schemas import AssetCreate, AssetRead
from app.modules.core.models import User

router = APIRouter(prefix="/assets", tags=["assets"])


@router.post("/", response_model=AssetRead, status_code=201)
async def register_asset(
    payload: AssetCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    """
    Registers asset metadata against an already-uploaded file. Actual
    binary storage (S3/GCS/local disk) is out of scope for this demo —
    `storage_path` is whatever the frontend's upload step produced.
    """
    asset = Asset(**payload.model_dump(), uploaded_by=current_user.id, status=AssetStatus.READY)
    db.add(asset)
    await db.commit()
    await db.refresh(asset)
    return asset


@router.get("/", response_model=list[AssetRead])
async def list_assets(
    project_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _current_user: User = Depends(get_current_active_user),
):
    result = await db.execute(select(Asset).where(Asset.project_id == project_id))
    return result.scalars().all()
