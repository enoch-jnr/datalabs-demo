import enum

from sqlalchemy import Column, Enum, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB, UUID

from app.core.database import Base
from app.core.mixins import ActiveMixin, TimestampMixin, UUIDMixin


class PipelineStatus(str, enum.Enum):
    IDLE = "IDLE"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class Pipeline(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "pipelines"
    __table_args__ = {"schema": "pipelines"}

    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.projects.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(150), nullable=False)
    status = Column(Enum(PipelineStatus), nullable=False, default=PipelineStatus.IDLE)
    definition = Column(JSONB, nullable=False, default=dict)
