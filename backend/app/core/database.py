from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.core.config import settings


class Base(DeclarativeBase):
    pass


engine = create_async_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    echo=settings.ENVIRONMENT == "development",
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)


async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


async def create_all_tables() -> None:
    """
    Demo-only convenience: creates schemas + tables directly from the ORM
    metadata. Swap this out for Alembic migrations (see /alembic) before
    anything resembling production use — create_all doesn't track schema
    changes, only creates what's missing on a fresh database.
    """
    schemas = sorted({table.schema for table in Base.metadata.tables.values() if table.schema})

    async with engine.begin() as conn:
        # every module puts its tables in its own Postgres schema
        # (core, projects, datasets, annotations, ...) — create_all()
        # only creates tables, not the schemas they live in, so those
        # have to be created explicitly first or every CREATE TABLE
        # for a non-public schema fails with "schema ... does not exist".
        for schema in schemas:
            await conn.execute(text(f'CREATE SCHEMA IF NOT EXISTS "{schema}"'))

        await conn.run_sync(Base.metadata.create_all)
