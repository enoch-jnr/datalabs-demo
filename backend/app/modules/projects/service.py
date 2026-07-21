import uuid

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.projects.models import Project
from app.modules.projects.schemas import ProjectCreate, ProjectUpdate
from app.modules.workspaces.models import Workspace


async def _get_owned_workspace(db: AsyncSession, workspace_id: uuid.UUID, user_id: uuid.UUID) -> Workspace:
    result = await db.execute(select(Workspace).where(Workspace.id == workspace_id))
    workspace = result.scalar_one_or_none()
    if workspace is None or workspace.owner_id != user_id:
        raise HTTPException(status_code=404, detail="Workspace not found")
    return workspace


async def create_project(db: AsyncSession, payload: ProjectCreate, user_id: uuid.UUID) -> Project:
    await _get_owned_workspace(db, payload.workspace_id, user_id)
    project = Project(**payload.model_dump(), owner_id=user_id)
    db.add(project)
    await db.commit()
    await db.refresh(project)
    return project


async def list_projects_for_workspace(db: AsyncSession, workspace_id: uuid.UUID) -> list[Project]:
    result = await db.execute(select(Project).where(Project.workspace_id == workspace_id))
    return list(result.scalars().all())


async def get_project(db: AsyncSession, project_id: uuid.UUID) -> Project:
    result = await db.execute(select(Project).where(Project.id == project_id))
    project = result.scalar_one_or_none()
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


async def update_project(db: AsyncSession, project_id: uuid.UUID, payload: ProjectUpdate) -> Project:
    project = await get_project(db, project_id)
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(project, field, value)
    await db.commit()
    await db.refresh(project)
    return project


async def delete_project(db: AsyncSession, project_id: uuid.UUID) -> None:
    project = await get_project(db, project_id)
    await db.delete(project)
    await db.commit()
