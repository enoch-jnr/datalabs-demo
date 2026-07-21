from sqlalchemy import BigInteger, Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base
from app.core.mixins import ActiveMixin, TimestampMixin, UUIDMixin


class StorageBucket(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "storage_buckets"
    __table_args__ = {"schema": "storage"}

    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.projects.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(150), nullable=False)
    provider = Column(String(50), nullable=False, default="LOCAL")
    quota_bytes = Column(BigInteger, nullable=False, default=0)
    used_bytes = Column(BigInteger, nullable=False, default=0)
