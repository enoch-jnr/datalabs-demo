from sqlalchemy import BigInteger, Column, Enum, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.core.mixins import ActiveMixin, TimestampMixin, UUIDMixin
from app.modules.assets.enums import AssetStatus, AssetType


class Asset(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "assets"
    __table_args__ = {"schema": "assets"}

    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.projects.id", ondelete="CASCADE"), nullable=False, index=True)
    uploaded_by = Column(UUID(as_uuid=True), ForeignKey("core.users.id", ondelete="SET NULL"), nullable=True)

    name = Column(String(255), nullable=False)
    asset_type = Column(Enum(AssetType), nullable=False)
    status = Column(Enum(AssetStatus), nullable=False, default=AssetStatus.UPLOADING)

    storage_path = Column(String(1000), nullable=False)
    mime_type = Column(String(120), nullable=True)
    file_size = Column(BigInteger, nullable=False, default=0)

    metadata_json = Column(JSONB, nullable=False, default=dict)

    project = relationship("Project", back_populates="assets")
    uploader = relationship("User", foreign_keys="Asset.uploaded_by")
    dataset_links = relationship("DatasetAsset", back_populates="asset", cascade="all, delete-orphan")
