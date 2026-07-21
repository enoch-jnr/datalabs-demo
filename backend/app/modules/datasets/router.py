import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import get_current_active_user
from app.modules.core.models import User
from app.modules.datasets import service
from app.modules.datasets.schemas import (
    DatasetAssetAdd,
    DatasetAssetRead,
    DatasetCreate,
    DatasetRead,
    DatasetVersionCreate,
    DatasetVersionRead,
)

router = APIRouter(prefix="/datasets", tags=["datasets"])


@router.post("/", response_model=DatasetRead, status_code=201)
async def create_dataset(
    payload: DatasetCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    return await service.create_dataset(db, payload, current_user.id)


@router.get("/", response_model=list[DatasetRead])
async def list_datasets(
    project_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _current_user: User = Depends(get_current_active_user),
):
    return await service.list_datasets(db, project_id)


@router.get("/{dataset_id}", response_model=DatasetRead)
async def get_dataset(
    dataset_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _current_user: User = Depends(get_current_active_user),
):
    return await service.get_dataset(db, dataset_id)


@router.post("/{dataset_id}/versions", response_model=DatasetVersionRead, status_code=201)
async def create_version(
    dataset_id: uuid.UUID,
    payload: DatasetVersionCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    return await service.create_version(db, dataset_id, payload, current_user.id)


@router.get("/{dataset_id}/versions", response_model=list[DatasetVersionRead])
async def list_versions(
    dataset_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _current_user: User = Depends(get_current_active_user),
):
    return await service.list_versions(db, dataset_id)


@router.post("/{dataset_id}/assets", response_model=DatasetAssetRead, status_code=201)
async def add_asset(
    dataset_id: uuid.UUID,
    payload: DatasetAssetAdd,
    db: AsyncSession = Depends(get_db),
    _current_user: User = Depends(get_current_active_user),
):
    return await service.add_asset_to_dataset(db, dataset_id, payload)
