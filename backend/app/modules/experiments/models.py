from sqlalchemy import Column, Enum, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB, UUID
import enum

from app.core.database import Base
from app.core.mixins import ActiveMixin, TimestampMixin, UUIDMixin


class ExperimentStatus(str, enum.Enum):
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class Experiment(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "experiments"
    __table_args__ = {"schema": "experiments"}

    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.projects.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(150), nullable=False)
    status = Column(Enum(ExperimentStatus), nullable=False, default=ExperimentStatus.RUNNING)
    metrics = Column(JSONB, nullable=False, default=dict)
    parameters = Column(JSONB, nullable=False, default=dict)
