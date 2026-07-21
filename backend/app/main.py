from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.database import create_all_tables

# --- deep MVP modules (real business logic) ---
from app.modules.core.router import router as auth_router
from app.modules.workspaces.router import router as workspaces_router
from app.modules.projects.router import router as projects_router
from app.modules.assets.router import router as assets_router
from app.modules.datasets.router import router as datasets_router
from app.modules.annotations.router import router as annotations_router
from app.modules.notifications.router import router as notifications_router
from app.modules.search.router import router as search_router

# --- scaffolded modules (generic CRUD, real DB-backed) ---
from app.modules.enterprises.router import router as enterprises_router
from app.modules.teams.router import router as teams_router
from app.modules.experiments.router import router as experiments_router
from app.modules.model_registry.router import router as model_registry_router
from app.modules.training.router import router as training_router
from app.modules.deployments.router import router as deployments_router
from app.modules.pipelines.router import router as pipelines_router
from app.modules.inference.router import router as inference_router
from app.modules.registry.router import router as registry_router
from app.modules.monitoring.router import router as monitoring_router
from app.modules.plugins.router import router as plugins_router
from app.modules.analytics.router import router as analytics_router
from app.modules.audit.router import router as audit_router
from app.modules.storage.router import router as storage_router
from app.modules.billing.router import router as billing_router
from app.modules.api_keys.router import router as api_keys_router
from app.modules.marketplace.router import router as marketplace_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Demo-only: creates tables from ORM metadata directly. Replace with
    # `alembic upgrade head` once you're tracking real schema migrations.
    await create_all_tables()
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_PREFIX = "/api/v1"

# deep MVP
app.include_router(auth_router, prefix=API_PREFIX)
app.include_router(workspaces_router, prefix=API_PREFIX)
app.include_router(projects_router, prefix=API_PREFIX)
app.include_router(assets_router, prefix=API_PREFIX)
app.include_router(datasets_router, prefix=API_PREFIX)
app.include_router(annotations_router, prefix=API_PREFIX)
app.include_router(notifications_router, prefix=API_PREFIX)
app.include_router(search_router, prefix=API_PREFIX)

# scaffolded
app.include_router(enterprises_router, prefix=API_PREFIX)
app.include_router(teams_router, prefix=API_PREFIX)
app.include_router(experiments_router, prefix=API_PREFIX)
app.include_router(model_registry_router, prefix=API_PREFIX)
app.include_router(training_router, prefix=API_PREFIX)
app.include_router(deployments_router, prefix=API_PREFIX)
app.include_router(pipelines_router, prefix=API_PREFIX)
app.include_router(inference_router, prefix=API_PREFIX)
app.include_router(registry_router, prefix=API_PREFIX)
app.include_router(monitoring_router, prefix=API_PREFIX)
app.include_router(plugins_router, prefix=API_PREFIX)
app.include_router(analytics_router, prefix=API_PREFIX)
app.include_router(audit_router, prefix=API_PREFIX)
app.include_router(storage_router, prefix=API_PREFIX)
app.include_router(billing_router, prefix=API_PREFIX)
app.include_router(api_keys_router, prefix=API_PREFIX)
app.include_router(marketplace_router, prefix=API_PREFIX)


@app.get("/health")
async def health():
    return {"status": "ok", "project": settings.PROJECT_NAME}
