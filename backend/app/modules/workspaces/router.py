import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import get_current_active_user
from app.modules.core.models import User
from app.modules.workspaces.models import Workspace
from app.modules.workspaces.schemas import WorkspaceCreate, WorkspaceRead

router = APIRouter(prefix="/workspaces", tags=["workspaces"])


@router.get("/", response_model=list[WorkspaceRead])
async def list_my_workspaces(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    result = await db.execute(select(Workspace).where(Workspace.owner_id == current_user.id))
    return result.scalars().all()


@router.post("/", response_model=WorkspaceRead, status_code=201)
async def create_workspace(
    payload: WorkspaceCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    workspace = Workspace(**payload.model_dump(), owner_id=current_user.id)
    db.add(workspace)
    await db.commit()
    await db.refresh(workspace)
    return workspace


@router.get("/{workspace_id}", response_model=WorkspaceRead)
async def get_workspace(
    workspace_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    result = await db.execute(select(Workspace).where(Workspace.id == workspace_id))
    workspace = result.scalar_one_or_none()
    if workspace is None or workspace.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Workspace not found")
    return workspace
