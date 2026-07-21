from sqlalchemy import Column, Enum, ForeignKey, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.core.mixins import ActiveMixin, TimestampMixin, UUIDMixin
from app.modules.projects.enums import ProjectStatus, ProjectVisibility


class Project(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "projects"
    __table_args__ = (
        UniqueConstraint("workspace_id", "code", name="uq_project_workspace_code"),
        {"schema": "projects"},
    )

    workspace_id = Column(UUID(as_uuid=True), ForeignKey("workspaces.workspaces.id", ondelete="CASCADE"), nullable=False, index=True)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("core.users.id", ondelete="SET NULL"), nullable=True)

    name = Column(String(150), nullable=False)
    code = Column(String(100), nullable=False)
    description = Column(String(1000), nullable=True)

    visibility = Column(Enum(ProjectVisibility), nullable=False, default=ProjectVisibility.PRIVATE)
    status = Column(Enum(ProjectStatus), nullable=False, default=ProjectStatus.DRAFT)

    metadata_json = Column(JSONB, nullable=False, default=dict)

    workspace = relationship("Workspace", back_populates="projects")
    owner = relationship("User", foreign_keys="Project.owner_id")

    datasets = relationship("Dataset", back_populates="project", cascade="all, delete-orphan")
    assets = relationship("Asset", back_populates="project", cascade="all, delete-orphan")
    annotation_tasks = relationship("AnnotationTask", back_populates="project", cascade="all, delete-orphan")
