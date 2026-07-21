import enum

from sqlalchemy import Column, Enum, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base
from app.core.mixins import ActiveMixin, TimestampMixin, UUIDMixin


class DeploymentStatus(str, enum.Enum):
    DEPLOYING = "DEPLOYING"
    LIVE = "LIVE"
    STOPPED = "STOPPED"
    FAILED = "FAILED"


class Deployment(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "deployments"
    __table_args__ = {"schema": "deployments"}

    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.projects.id", ondelete="CASCADE"), nullable=False, index=True)
    model_id = Column(UUID(as_uuid=True), ForeignKey("model_registry.ml_models.id", ondelete="SET NULL"), nullable=True, index=True)

    name = Column(String(150), nullable=False)
    endpoint_url = Column(String(500), nullable=True)
    status = Column(Enum(DeploymentStatus), nullable=False, default=DeploymentStatus.DEPLOYING)
