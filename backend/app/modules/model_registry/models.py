import enum

from sqlalchemy import Column, Enum, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB, UUID

from app.core.database import Base
from app.core.mixins import ActiveMixin, TimestampMixin, UUIDMixin


class ModelStage(str, enum.Enum):
    STAGING = "STAGING"
    PRODUCTION = "PRODUCTION"
    ARCHIVED = "ARCHIVED"


class MLModel(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "ml_models"
    __table_args__ = {"schema": "model_registry"}

    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.projects.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(150), nullable=False)
    description = Column(String(1000), nullable=True)
    stage = Column(Enum(ModelStage), nullable=False, default=ModelStage.STAGING)
    metadata_json = Column(JSONB, nullable=False, default=dict)
