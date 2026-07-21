import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.modules.assets.enums import AssetStatus, AssetType


class AssetBase(BaseModel):
    name: str
    asset_type: AssetType
    mime_type: str | None = None


class AssetCreate(AssetBase):
    project_id: uuid.UUID
    storage_path: str
    file_size: int = 0


class AssetRead(AssetBase):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    project_id: uuid.UUID
    status: AssetStatus
    storage_path: str
    file_size: int
    created_at: datetime
