import enum

from sqlalchemy import Column, Enum, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base
from app.core.mixins import ActiveMixin, TimestampMixin, UUIDMixin


class AlertSeverity(str, enum.Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class MonitoringAlert(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "monitoring_alerts"
    __table_args__ = {"schema": "monitoring"}

    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.projects.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(150), nullable=False)
    severity = Column(Enum(AlertSeverity), nullable=False, default=AlertSeverity.LOW)
    message = Column(String(2000), nullable=True)
