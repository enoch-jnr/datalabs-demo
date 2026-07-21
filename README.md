# DataLabs Demo

> **OpenAI Build Week 2026 Submission**

DataLabs Demo is a proof-of-concept AI data platform built during the OpenAI Build Week hackathon using **GPT-5.6** and **Codex**. It demonstrates the core architecture of a modern AI data management platform rather than a production-ready system.

The project showcases a full-stack architecture consisting of:

* **FastAPI** backend
* **React + TypeScript + Vite** frontend
* **PostgreSQL** database
* **Redis** for caching and background services
* **Docker Compose** for local development
* **JWT Authentication**
* **Async SQLAlchemy ORM**
* **Material UI + Tailwind CSS**

The primary goal was to validate the platform architecture, workflows, and developer experience within the hackathon timeframe.

---

# Project Scope

Rather than building a fully production-ready platform, this project focuses on demonstrating the complete architecture with representative implementations.

### Fully Implemented Modules

The following modules include custom business logic and complete workflows:

* Authentication

  * User registration
  * Login
  * JWT authentication
  * Refresh tokens
  * Current user profile

* Workspaces & Projects

  * Personal workspace creation
  * Project ownership
  * Project management

* Datasets

  * Dataset creation
  * Dataset versions
  * Asset relationships

* Annotations

  * Annotation tasks
  * Task assignments
  * Label submission
  * Review workflow

* Notifications

  * Notification listing
  * Mark as read
  * User preferences

* Search

  * Cross-module search
  * Projects
  * Datasets
  * Annotation tasks

---

# Platform Architecture

The remaining platform modules demonstrate the intended architecture using shared CRUD services and database models.

These include:

* Enterprises
* Teams
* Experiments
* Model Registry
* Training
* Deployments
* Pipelines
* Inference
* Registry
* Monitoring
* Plugins
* Analytics
* Audit
* Storage
* Billing
* API Keys
* Marketplace

These modules already include:

* SQLAlchemy models
* Database relationships
* FastAPI CRUD endpoints
* Shared service architecture
* Generic frontend pages

However, they intentionally do **not** yet include advanced production workflows such as orchestration engines, approval systems, deployment pipelines, or distributed processing.

This design choice allowed the project to demonstrate the complete platform architecture while remaining achievable within the Build Week timeframe.

---

# Special Implementations

Although most modules use the shared CRUD architecture, a few include additional functionality.

### API Keys

Implements secure one-time secret generation and retrieval rather than standard CRUD operations.

### Audit

Includes centralized audit logging with authentication events already recorded. The remaining modules are structured so additional audit events can easily be added as development continues.

---

# Running the Demo

### Backend

```bash
cd backend
cp .env.example .env
docker compose up --build
```

This starts:

* PostgreSQL
* Redis
* FastAPI Backend

The backend currently creates database tables directly from SQLAlchemy metadata during startup.

**Note:** This is a hackathon shortcut and should be replaced with Alembic migrations in future development.

API documentation is available at:

```
http://localhost:8000/docs
```

---

### Frontend

```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```

Open:

```
http://localhost:5173
```

New users can register immediately. A personal workspace is automatically created to simplify the demo experience.

---

# Future Roadmap

The next development milestones include:

1. Replace automatic table creation with Alembic migrations.
2. Implement real file storage (S3, Azure Blob, or local storage).
3. Complete the Enterprise → Team → Workspace workflow.
4. Build the complete Model Registry → Training → Deployment → Inference lifecycle.
5. Add OAuth authentication (Google and GitHub).
6. Deploy using Kubernetes for production environments.

---

# Technology Stack

### Backend

* FastAPI
* Async SQLAlchemy
* PostgreSQL
* Redis
* Docker
* JWT Authentication

### Frontend

* React
* TypeScript
* Vite
* Material UI
* Tailwind CSS

---

# Built with GPT-5.6 and Codex

This project was developed during **OpenAI Build Week** using **GPT-5.6** and **Codex**.

Codex accelerated development by assisting with:

* Backend architecture
* API scaffolding
* Database models
* CRUD generation
* Frontend page generation
* Component structure
* Folder organization
* Refactoring
* Debugging
* Documentation

GPT-5.6 was used throughout the project for architectural planning, reasoning, implementation guidance, and iterative problem solving.

---

# Disclaimer

This repository is **not a production-ready platform**. It is a hackathon demonstration intended to showcase the architecture, workflows, and development approach behind DataLabs. Several advanced features have been intentionally deferred to future iterations to prioritize delivering a functional end-to-end prototype within the Build Week timeline.
