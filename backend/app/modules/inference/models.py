import enum

from sqlalchemy import Column, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB, UUID

from app.core.database import Base
from app.core.mixins import TimestampMixin, UUIDMixin


class InferenceStatus(str, enum.Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class InferenceRequest(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "inference_requests"
    __table_args__ = {"schema": "inference"}

    deployment_id = Column(UUID(as_uuid=True), ForeignKey("deployments.deployments.id", ondelete="CASCADE"), nullable=False, index=True)
    input_data = Column(JSONB, nullable=False, default=dict)
    output_data = Column(JSONB, nullable=False, default=dict)
    status = Column(Enum(InferenceStatus), nullable=False, default=InferenceStatus.PENDING)
