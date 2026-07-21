import asyncio
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config

from alembic import context

from app.core.config import settings
from app.core.database import Base

# import every module's models so they register on Base.metadata
from app.modules.core import models as core_models  # noqa: F401
from app.modules.workspaces import models as workspaces_models  # noqa: F401
from app.modules.projects import models as projects_models  # noqa: F401
from app.modules.assets import models as assets_models  # noqa: F401
from app.modules.datasets import models as datasets_models  # noqa: F401
from app.modules.annotations import models as annotations_models  # noqa: F401
from app.modules.notifications import models as notifications_models  # noqa: F401
from app.modules.enterprises import models as enterprises_models  # noqa: F401
from app.modules.teams import models as teams_models  # noqa: F401
from app.modules.experiments import models as experiments_models  # noqa: F401
from app.modules.model_registry import models as model_registry_models  # noqa: F401
from app.modules.training import models as training_models  # noqa: F401
from app.modules.deployments import models as deployments_models  # noqa: F401
from app.modules.pipelines import models as pipelines_models  # noqa: F401
from app.modules.inference import models as inference_models  # noqa: F401
from app.modules.registry import models as registry_models  # noqa: F401
from app.modules.monitoring import models as monitoring_models  # noqa: F401
from app.modules.plugins import models as plugins_models  # noqa: F401
from app.modules.analytics import models as analytics_models  # noqa: F401
from app.modules.audit import models as audit_models  # noqa: F401
from app.modules.storage import models as storage_models  # noqa: F401
from app.modules.billing import models as billing_models  # noqa: F401
from app.modules.api_keys import models as api_keys_models  # noqa: F401
from app.modules.marketplace import models as marketplace_models  # noqa: F401

config = context.config
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
