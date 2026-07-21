import uuid
from typing import Generic, Type, TypeVar

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import Base, get_db
from app.core.dependencies import get_current_active_user

ModelT = TypeVar("ModelT", bound=Base)
ReadSchemaT = TypeVar("ReadSchemaT", bound=BaseModel)
CreateSchemaT = TypeVar("CreateSchemaT", bound=BaseModel)


class GenericCRUDRouter(Generic[ModelT, ReadSchemaT, CreateSchemaT]):
    """
    Builds a basic list/get/create/delete router for a model, gated
    behind the same JWT auth as everything else.

    This exists so every scaffolded module (the ones without bespoke
    business logic yet) gets a real, working REST surface — backed by
    the actual database — instead of static mock JSON. Modules with
    real workflows (auth, projects, datasets, annotations, notifications,
    search, api_keys) have their own hand-written routers instead of this.
    """

    def __init__(
        self,
        model: Type[ModelT],
        read_schema: Type[ReadSchemaT],
        create_schema: Type[CreateSchemaT],
        prefix: str,
        tags: list[str],
    ):
        self.model = model
        self.read_schema = read_schema
        self.create_schema = create_schema
        self.router = APIRouter(prefix=prefix, tags=tags)
        self._register_routes()

    def _register_routes(self) -> None:
        model = self.model
        read_schema = self.read_schema
        create_schema = self.create_schema

        @self.router.get("/", response_model=list[read_schema])
        async def list_items(
            skip: int = 0,
            limit: int = 50,
            db: AsyncSession = Depends(get_db),
            _user=Depends(get_current_active_user),
        ):
            result = await db.execute(select(model).offset(skip).limit(limit))
            return result.scalars().all()

        @self.router.get("/{item_id}", response_model=read_schema)
        async def get_item(
            item_id: uuid.UUID,
            db: AsyncSession = Depends(get_db),
            _user=Depends(get_current_active_user),
        ):
            result = await db.execute(select(model).where(model.id == item_id))
            item = result.scalar_one_or_none()
            if item is None:
                raise HTTPException(status_code=404, detail=f"{model.__name__} not found")
            return item

        @self.router.post("/", response_model=read_schema, status_code=201)
        async def create_item(
            payload: create_schema,
            db: AsyncSession = Depends(get_db),
            _user=Depends(get_current_active_user),
        ):
            item = model(**payload.model_dump())
            db.add(item)
            await db.commit()
            await db.refresh(item)
            return item

        @self.router.delete("/{item_id}", status_code=204)
        async def delete_item(
            item_id: uuid.UUID,
            db: AsyncSession = Depends(get_db),
            _user=Depends(get_current_active_user),
        ):
            result = await db.execute(select(model).where(model.id == item_id))
            item = result.scalar_one_or_none()
            if item is None:
                raise HTTPException(status_code=404, detail=f"{model.__name__} not found")
            await db.delete(item)
            await db.commit()
