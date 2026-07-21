from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.core.mixins import ActiveMixin, TimestampMixin, UUIDMixin
from app.modules.annotations.enums import AnnotationShape, AnnotationStatus, AnnotationType, AssignmentStatus


class AnnotationClass(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "annotation_classes"
    __table_args__ = {"schema": "annotations"}

    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.projects.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(150), nullable=False)
    color = Column(String(20), nullable=False, default="#4285F4")

    labels = relationship("AnnotationLabel", back_populates="annotation_class")


class AnnotationTask(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "annotation_tasks"
    __table_args__ = {"schema": "annotations"}

    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.projects.id", ondelete="CASCADE"), nullable=False, index=True)
    dataset_id = Column(UUID(as_uuid=True), ForeignKey("datasets.datasets.id", ondelete="SET NULL"), nullable=True, index=True)
    created_by = Column(UUID(as_uuid=True), ForeignKey("core.users.id", ondelete="SET NULL"), nullable=True)

    name = Column(String(150), nullable=False)
    instructions = Column(String(4000), nullable=True)
    annotation_type = Column(Enum(AnnotationType), nullable=False)
    status = Column(Enum(AnnotationStatus), nullable=False, default=AnnotationStatus.NOT_STARTED)
    due_date = Column(DateTime(timezone=True), nullable=True)

    project = relationship("Project", back_populates="annotation_tasks")
    dataset = relationship("Dataset", back_populates="annotation_tasks")
    creator = relationship("User", foreign_keys="AnnotationTask.created_by")

    assignments = relationship("AnnotationAssignment", back_populates="task", cascade="all, delete-orphan")
    annotations = relationship("Annotation", back_populates="task", cascade="all, delete-orphan")


class AnnotationAssignment(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "annotation_assignments"
    __table_args__ = {"schema": "annotations"}

    task_id = Column(UUID(as_uuid=True), ForeignKey("annotations.annotation_tasks.id", ondelete="CASCADE"), nullable=False, index=True)
    dataset_asset_id = Column(UUID(as_uuid=True), ForeignKey("datasets.dataset_assets.id", ondelete="CASCADE"), nullable=False, index=True)
    assigned_to = Column(UUID(as_uuid=True), ForeignKey("core.users.id", ondelete="CASCADE"), nullable=False, index=True)

    status = Column(Enum(AssignmentStatus), nullable=False, default=AssignmentStatus.ASSIGNED)

    task = relationship("AnnotationTask", back_populates="assignments")
    dataset_asset = relationship("DatasetAsset")
    annotator = relationship("User", foreign_keys="AnnotationAssignment.assigned_to")


class Annotation(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "annotations"
    __table_args__ = {"schema": "annotations"}

    task_id = Column(UUID(as_uuid=True), ForeignKey("annotations.annotation_tasks.id", ondelete="CASCADE"), nullable=False, index=True)
    dataset_asset_id = Column(UUID(as_uuid=True), ForeignKey("datasets.dataset_assets.id", ondelete="CASCADE"), nullable=False, index=True)
    created_by = Column(UUID(as_uuid=True), ForeignKey("core.users.id", ondelete="SET NULL"), nullable=True)

    status = Column(Enum(AnnotationStatus), nullable=False, default=AnnotationStatus.NOT_STARTED)

    task = relationship("AnnotationTask", back_populates="annotations")
    dataset_asset = relationship("DatasetAsset", back_populates="annotations")
    creator = relationship("User", foreign_keys="Annotation.created_by")

    labels = relationship("AnnotationLabel", back_populates="annotation", cascade="all, delete-orphan")


class AnnotationLabel(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "annotation_labels"
    __table_args__ = {"schema": "annotations"}

    annotation_id = Column(UUID(as_uuid=True), ForeignKey("annotations.annotations.id", ondelete="CASCADE"), nullable=False, index=True)
    annotation_class_id = Column(UUID(as_uuid=True), ForeignKey("annotations.annotation_classes.id", ondelete="SET NULL"), nullable=True, index=True)

    shape = Column(Enum(AnnotationShape), nullable=False, default=AnnotationShape.LABEL)
    geometry = Column(JSONB, nullable=False, default=dict)
    text_value = Column(String(2000), nullable=True)
    display_order = Column(Integer, nullable=False, default=0)

    annotation = relationship("Annotation", back_populates="labels")
    annotation_class = relationship("AnnotationClass", back_populates="labels")
