# DataLabs Demo

A working demo of the DataLabs architecture: FastAPI + async SQLAlchemy +
Postgres backend, React + TypeScript + MUI + Tailwind frontend, JWT auth,
all 24 modules present.

Verified this session: backend imports cleanly (103 routes), full
`py_compile` pass on every backend file, frontend `tsc -b` type-checks
clean, and `vite build` produces a working production bundle.

## Depth: Deep MVP vs. scaffolded

Per your call, six modules are fully wired end-to-end (real service
layers, real workflows, matching frontend pages):

- **auth** — register/login/refresh/me, JWT (access + refresh tokens)
- **workspaces → projects** — the ownership chain projects hang off
- **datasets** — dataset → version → asset linking
- **annotations** — task → assignment → submit (with labels) → review
- **notifications** — list/mark-read/preferences
- **search** — real ILIKE search across projects/datasets/annotation tasks

The other 17 modules (enterprises, teams, experiments, model_registry,
training, deployments, pipelines, inference, registry, monitoring,
plugins, analytics, audit, storage, billing, api_keys, marketplace) have
real SQLAlchemy models and a real, database-backed CRUD API — via a
shared `GenericCRUDRouter` factory on the backend and a matching
`GenericModulePage` component on the frontend — but no bespoke business
logic yet (no approval workflows, no training orchestration, etc.). This
was the explicit tradeoff for "wide but real API surface, without
writing 17 modules' worth of custom logic."

`api_keys` is the one exception in the scaffolded group — it has real
logic (one-time secret reveal) since generic CRUD can't do that safely.

`audit` also has a real `log_action()` helper already called from
login/register, so the "central audit logging" goal has at least one
genuine, working caller — extend the calls into the other modules'
service layers as you build them out.

## Running it

```bash
cd backend
cp .env.example .env       # edit JWT_SECRET_KEY etc for anything beyond local demo use
docker compose up --build
```

This starts Postgres (`datalabs_demo` db), Redis, and the backend on
`:8000`. Tables are created directly from ORM metadata on startup
(`create_all_tables()` in `app/main.py`) — that's a demo shortcut, not a
migration strategy. Swap to Alembic before anything resembling
production:

```bash
cd backend
alembic revision --autogenerate -m "init"
alembic upgrade head
```

(The `alembic/env.py` is already wired for async SQLAlchemy and imports
every module's models — autogenerate should pick up the full schema.)

Frontend:

```bash
cd frontend
npm install
cp .env.example .env       # VITE_API_BASE_URL, defaults to localhost:8000
npm run dev
```

Visit `http://localhost:5173`. Sign up with any email — a personal
workspace is created automatically on first dashboard load so you have
somewhere for projects to live (Enterprise → Team → Workspace is
present as real scaffolded modules, but the demo doesn't force you
through that chain to get started).

API docs: `http://localhost:8000/docs` (FastAPI's automatic Swagger UI —
useful for poking at the 17 scaffolded modules directly).

## What to build next, in order

1. **Alembic migrations** — replace `create_all_tables()` before this
   touches a real database anyone depends on.
2. **Real file upload** for `assets` — right now `/assets/` only
   registers metadata against a `storage_path` the frontend already
   has; there's no actual S3/GCS/local disk handler yet.
3. **Enterprise → Team → Workspace chain** — `workspaces.enterprise_id`
   is already a nullable pointer waiting for `enterprises`/`teams` to
   grow past generic CRUD.
4. **Model Registry → Training → Deployment → Inference loop** — the
   models exist and reference each other (`Deployment.model_id →
   MLModel.id`), but there's no orchestration logic connecting them yet.
5. **OAuth2 (Google/GitHub)** — config fields for client id/secret
   already exist in `app/core/config.py`, unused. Standard `authlib` +
   FastAPI OAuth flow slots in there.
6. **Kubernetes manifests** — only Docker Compose exists right now;
   the Dockerfile is a reasonable base for a k8s Deployment.

## Notable naming choice

The "Models" module from your architecture doc (model registry) is
named `model_registry` in code — `models` would collide with the
`app/modules/<name>/models.py` convention used by every other module.
