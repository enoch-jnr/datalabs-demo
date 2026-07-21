from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB, UUID

from app.core.database import Base
from app.core.mixins import ActiveMixin, TimestampMixin, UUIDMixin


class Dashboard(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "dashboards"
    __table_args__ = {"schema": "analytics"}

    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.projects.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(150), nullable=False)
    widgets_config = Column(JSONB, nullable=False, default=list)
