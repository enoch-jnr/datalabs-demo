from sqlalchemy import Column, ForeignKey, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.core.mixins import ActiveMixin, TimestampMixin, UUIDMixin


class Workspace(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "workspaces"
    __table_args__ = (
        UniqueConstraint("owner_id", "slug", name="uq_workspace_owner_slug"),
        {"schema": "workspaces"},
    )

    # Nullable so a workspace can later be re-parented under an Enterprise
    # once that module grows past its scaffold — not wired for the demo.
    enterprise_id = Column(UUID(as_uuid=True), nullable=True, index=True)

    owner_id = Column(UUID(as_uuid=True), ForeignKey("core.users.id", ondelete="CASCADE"), nullable=False, index=True)

    name = Column(String(150), nullable=False)
    slug = Column(String(100), nullable=False)
    description = Column(String(1000), nullable=True)

    owner = relationship("User", back_populates="workspaces")
    projects = relationship("Project", back_populates="workspace", cascade="all, delete-orphan")
