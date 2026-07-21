import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import get_current_active_user
from app.modules.annotations import service
from app.modules.annotations.schemas import (
    AnnotationRead,
    AnnotationReviewDecision,
    AnnotationSubmit,
    AnnotationTaskCreate,
    AnnotationTaskRead,
    AssignmentCreate,
    AssignmentRead,
)
from app.modules.core.models import User

router = APIRouter(prefix="/annotations", tags=["annotations"])


@router.post("/tasks", response_model=AnnotationTaskRead, status_code=201)
async def create_task(
    payload: AnnotationTaskCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    return await service.create_task(db, payload, current_user.id)


@router.get("/tasks", response_model=list[AnnotationTaskRead])
async def list_tasks(
    project_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _current_user: User = Depends(get_current_active_user),
):
    return await service.list_tasks(db, project_id)


@router.post("/tasks/{task_id}/assignments", response_model=AssignmentRead, status_code=201)
async def assign_asset(
    task_id: uuid.UUID,
    payload: AssignmentCreate,
    db: AsyncSession = Depends(get_db),
    _current_user: User = Depends(get_current_active_user),
):
    return await service.assign_asset(db, task_id, payload)


@router.get("/assignments/mine", response_model=list[AssignmentRead])
async def my_assignments(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    return await service.list_my_assignments(db, current_user.id)


@router.post("/tasks/{task_id}/submit", response_model=AnnotationRead, status_code=201)
async def submit_annotation(
    task_id: uuid.UUID,
    payload: AnnotationSubmit,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    return await service.submit_annotation(db, task_id, payload, current_user.id)


@router.get("/{annotation_id}", response_model=AnnotationRead)
async def get_annotation(
    annotation_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _current_user: User = Depends(get_current_active_user),
):
    return await service.get_annotation(db, annotation_id)


@router.post("/{annotation_id}/review", response_model=AnnotationRead)
async def review_annotation(
    annotation_id: uuid.UUID,
    payload: AnnotationReviewDecision,
    db: AsyncSession = Depends(get_db),
    _current_user: User = Depends(get_current_active_user),
):
    return await service.review_annotation(db, annotation_id, payload)
