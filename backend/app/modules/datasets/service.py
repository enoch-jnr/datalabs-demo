import uuid

from fastapi import HTTPException
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.datasets.models import Dataset, DatasetAsset, DatasetVersion
from app.modules.datasets.schemas import DatasetAssetAdd, DatasetCreate, DatasetVersionCreate


async def create_dataset(db: AsyncSession, payload: DatasetCreate, owner_id: uuid.UUID) -> Dataset:
    dataset = Dataset(**payload.model_dump(), owner_id=owner_id)
    db.add(dataset)
    await db.commit()
    await db.refresh(dataset)

    # every dataset starts life with a v1 so uploads have somewhere to land
    initial_version = DatasetVersion(dataset_id=dataset.id, version=1, created_by=owner_id)
    db.add(initial_version)
    await db.commit()

    return dataset


async def list_datasets(db: AsyncSession, project_id: uuid.UUID) -> list[Dataset]:
    result = await db.execute(select(Dataset).where(Dataset.project_id == project_id))
    return list(result.scalars().all())


async def get_dataset(db: AsyncSession, dataset_id: uuid.UUID) -> Dataset:
    result = await db.execute(select(Dataset).where(Dataset.id == dataset_id))
    dataset = result.scalar_one_or_none()
    if dataset is None:
        raise HTTPException(status_code=404, detail="Dataset not found")
    return dataset


async def create_version(db: AsyncSession, dataset_id: uuid.UUID, payload: DatasetVersionCreate, user_id: uuid.UUID) -> DatasetVersion:
    await get_dataset(db, dataset_id)
    version = DatasetVersion(dataset_id=dataset_id, created_by=user_id, **payload.model_dump())
    db.add(version)
    await db.commit()
    await db.refresh(version)
    return version


async def list_versions(db: AsyncSession, dataset_id: uuid.UUID) -> list[DatasetVersion]:
    result = await db.execute(select(DatasetVersion).where(DatasetVersion.dataset_id == dataset_id))
    return list(result.scalars().all())


async def add_asset_to_dataset(db: AsyncSession, dataset_id: uuid.UUID, payload: DatasetAssetAdd) -> DatasetAsset:
    dataset = await get_dataset(db, dataset_id)
    link = DatasetAsset(dataset_id=dataset_id, **payload.model_dump())
    db.add(link)

    dataset.total_assets = (
        await db.execute(select(func.count()).select_from(DatasetAsset).where(DatasetAsset.dataset_id == dataset_id))
    ).scalar_one() + 1

    await db.commit()
    await db.refresh(link)
    return link
