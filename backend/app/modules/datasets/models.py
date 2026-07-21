from sqlalchemy import Column, Enum, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.core.mixins import ActiveMixin, TimestampMixin, UUIDMixin
from app.modules.datasets.enums import DatasetSplit, DatasetStatus, DatasetVisibility


class Dataset(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "datasets"
    __table_args__ = (
        UniqueConstraint("project_id", "code", name="uq_dataset_project_code"),
        {"schema": "datasets"},
    )

    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.projects.id", ondelete="CASCADE"), nullable=False, index=True)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("core.users.id", ondelete="SET NULL"), nullable=True)

    name = Column(String(255), nullable=False)
    code = Column(String(120), nullable=False)
    description = Column(String(5000), nullable=True)

    status = Column(Enum(DatasetStatus), nullable=False, default=DatasetStatus.DRAFT)
    visibility = Column(Enum(DatasetVisibility), nullable=False, default=DatasetVisibility.PRIVATE)

    metadata_json = Column(JSONB, nullable=False, default=dict)
    total_assets = Column(Integer, nullable=False, default=0)

    project = relationship("Project", back_populates="datasets")
    owner = relationship("User", foreign_keys="Dataset.owner_id")

    versions = relationship("DatasetVersion", back_populates="dataset", cascade="all, delete-orphan")
    assets = relationship("DatasetAsset", back_populates="dataset", cascade="all, delete-orphan")
    annotation_tasks = relationship("AnnotationTask", back_populates="dataset")


class DatasetVersion(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "dataset_versions"
    __table_args__ = (
        UniqueConstraint("dataset_id", "version", name="uq_dataset_version"),
        {"schema": "datasets"},
    )

    dataset_id = Column(UUID(as_uuid=True), ForeignKey("datasets.datasets.id", ondelete="CASCADE"), nullable=False, index=True)
    created_by = Column(UUID(as_uuid=True), ForeignKey("core.users.id", ondelete="SET NULL"), nullable=True)

    version = Column(Integer, nullable=False)
    changelog = Column(String(2000), nullable=True)
    status = Column(Enum(DatasetStatus), nullable=False, default=DatasetStatus.DRAFT)

    dataset = relationship("Dataset", back_populates="versions")
    creator = relationship("User", foreign_keys="DatasetVersion.created_by")
    assets = relationship("DatasetAsset", back_populates="dataset_version", cascade="all, delete-orphan")


class DatasetAsset(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "dataset_assets"
    __table_args__ = (
        UniqueConstraint("dataset_version_id", "asset_id", name="uq_dataset_version_asset"),
        {"schema": "datasets"},
    )

    dataset_id = Column(UUID(as_uuid=True), ForeignKey("datasets.datasets.id", ondelete="CASCADE"), nullable=False)
    dataset_version_id = Column(UUID(as_uuid=True), ForeignKey("datasets.dataset_versions.id", ondelete="CASCADE"), nullable=False)
    asset_id = Column(UUID(as_uuid=True), ForeignKey("assets.assets.id", ondelete="CASCADE"), nullable=False)

    split = Column(Enum(DatasetSplit), nullable=False, default=DatasetSplit.UNASSIGNED)
    metadata_json = Column(JSONB, nullable=False, default=dict)

    dataset = relationship("Dataset", back_populates="assets")
    dataset_version = relationship("DatasetVersion", back_populates="assets")
    asset = relationship("Asset", back_populates="dataset_links")

    annotations = relationship("Annotation", back_populates="dataset_asset", cascade="all, delete-orphan")
