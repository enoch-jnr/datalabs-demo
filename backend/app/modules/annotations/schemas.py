import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.modules.annotations.enums import AnnotationShape, AnnotationStatus, AnnotationType, AssignmentStatus


class AnnotationTaskCreate(BaseModel):
    project_id: uuid.UUID
    dataset_id: uuid.UUID | None = None
    name: str
    instructions: str | None = None
    annotation_type: AnnotationType


class AnnotationTaskRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    project_id: uuid.UUID
    dataset_id: uuid.UUID | None
    name: str
    annotation_type: AnnotationType
    status: AnnotationStatus
    created_at: datetime


class AssignmentCreate(BaseModel):
    dataset_asset_id: uuid.UUID
    assigned_to: uuid.UUID


class AssignmentRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    task_id: uuid.UUID
    dataset_asset_id: uuid.UUID
    assigned_to: uuid.UUID
    status: AssignmentStatus


class AnnotationLabelInput(BaseModel):
    annotation_class_id: uuid.UUID | None = None
    shape: AnnotationShape = AnnotationShape.LABEL
    geometry: dict = {}
    text_value: str | None = None


class AnnotationSubmit(BaseModel):
    dataset_asset_id: uuid.UUID
    labels: list[AnnotationLabelInput]


class AnnotationLabelRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    annotation_class_id: uuid.UUID | None
    shape: AnnotationShape
    geometry: dict
    text_value: str | None


class AnnotationRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    task_id: uuid.UUID
    dataset_asset_id: uuid.UUID
    status: AnnotationStatus
    labels: list[AnnotationLabelRead] = []


class AnnotationReviewDecision(BaseModel):
    approve: bool
    notes: str | None = None
