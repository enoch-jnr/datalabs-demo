import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.modules.datasets.enums import DatasetSplit, DatasetStatus, DatasetVisibility


class DatasetBase(BaseModel):
    name: str
    code: str
    description: str | None = None
    visibility: DatasetVisibility = DatasetVisibility.PRIVATE


class DatasetCreate(DatasetBase):
    project_id: uuid.UUID


class DatasetRead(DatasetBase):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    project_id: uuid.UUID
    status: DatasetStatus
    total_assets: int
    created_at: datetime


class DatasetVersionCreate(BaseModel):
    version: int
    changelog: str | None = None


class DatasetVersionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    dataset_id: uuid.UUID
    version: int
    changelog: str | None
    status: DatasetStatus
    created_at: datetime


class DatasetAssetAdd(BaseModel):
    dataset_version_id: uuid.UUID
    asset_id: uuid.UUID
    split: DatasetSplit = DatasetSplit.UNASSIGNED


class DatasetAssetRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    dataset_id: uuid.UUID
    dataset_version_id: uuid.UUID
    asset_id: uuid.UUID
    split: DatasetSplit
