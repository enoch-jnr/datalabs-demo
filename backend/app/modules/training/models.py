import enum

from sqlalchemy import Column, Enum, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB, UUID

from app.core.database import Base
from app.core.mixins import ActiveMixin, TimestampMixin, UUIDMixin


class TrainingJobStatus(str, enum.Enum):
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class TrainingJob(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "training_jobs"
    __table_args__ = {"schema": "training"}

    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.projects.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(150), nullable=False)
    status = Column(Enum(TrainingJobStatus), nullable=False, default=TrainingJobStatus.QUEUED)
    configuration = Column(JSONB, nullable=False, default=dict)
