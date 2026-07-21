import uuid

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.modules.annotations.enums import AnnotationStatus, AssignmentStatus
from app.modules.annotations.models import Annotation, AnnotationAssignment, AnnotationLabel, AnnotationTask
from app.modules.annotations.schemas import AnnotationSubmit, AssignmentCreate, AnnotationTaskCreate, AnnotationReviewDecision


async def create_task(db: AsyncSession, payload: AnnotationTaskCreate, user_id: uuid.UUID) -> AnnotationTask:
    task = AnnotationTask(**payload.model_dump(), created_by=user_id)
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


async def list_tasks(db: AsyncSession, project_id: uuid.UUID) -> list[AnnotationTask]:
    result = await db.execute(select(AnnotationTask).where(AnnotationTask.project_id == project_id))
    return list(result.scalars().all())


async def get_task(db: AsyncSession, task_id: uuid.UUID) -> AnnotationTask:
    result = await db.execute(select(AnnotationTask).where(AnnotationTask.id == task_id))
    task = result.scalar_one_or_none()
    if task is None:
        raise HTTPException(status_code=404, detail="Annotation task not found")
    return task


async def assign_asset(db: AsyncSession, task_id: uuid.UUID, payload: AssignmentCreate) -> AnnotationAssignment:
    await get_task(db, task_id)
    assignment = AnnotationAssignment(task_id=task_id, **payload.model_dump())
    db.add(assignment)
    await db.commit()
    await db.refresh(assignment)
    return assignment


async def list_my_assignments(db: AsyncSession, user_id: uuid.UUID) -> list[AnnotationAssignment]:
    result = await db.execute(select(AnnotationAssignment).where(AnnotationAssignment.assigned_to == user_id))
    return list(result.scalars().all())


async def submit_annotation(db: AsyncSession, task_id: uuid.UUID, payload: AnnotationSubmit, user_id: uuid.UUID) -> Annotation:
    await get_task(db, task_id)

    annotation = Annotation(
        task_id=task_id,
        dataset_asset_id=payload.dataset_asset_id,
        created_by=user_id,
        status=AnnotationStatus.SUBMITTED,
    )
    db.add(annotation)
    await db.flush()  # get annotation.id before attaching labels

    for label_input in payload.labels:
        db.add(AnnotationLabel(annotation_id=annotation.id, **label_input.model_dump()))

    # mark the matching assignment (if any) as submitted
    result = await db.execute(
        select(AnnotationAssignment).where(
            AnnotationAssignment.task_id == task_id,
            AnnotationAssignment.dataset_asset_id == payload.dataset_asset_id,
            AnnotationAssignment.assigned_to == user_id,
        )
    )
    assignment = result.scalar_one_or_none()
    if assignment is not None:
        assignment.status = AssignmentStatus.SUBMITTED

    await db.commit()

    result = await db.execute(
        select(Annotation).options(selectinload(Annotation.labels)).where(Annotation.id == annotation.id)
    )
    return result.scalar_one()


async def get_annotation(db: AsyncSession, annotation_id: uuid.UUID) -> Annotation:
    result = await db.execute(
        select(Annotation).options(selectinload(Annotation.labels)).where(Annotation.id == annotation_id)
    )
    annotation = result.scalar_one_or_none()
    if annotation is None:
        raise HTTPException(status_code=404, detail="Annotation not found")
    return annotation


async def review_annotation(db: AsyncSession, annotation_id: uuid.UUID, payload: AnnotationReviewDecision) -> Annotation:
    annotation = await get_annotation(db, annotation_id)
    annotation.status = AnnotationStatus.APPROVED if payload.approve else AnnotationStatus.REJECTED
    await db.commit()
    await db.refresh(annotation)
    return annotation
