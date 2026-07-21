from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.annotations.models import AnnotationTask
from app.modules.datasets.models import Dataset
from app.modules.projects.models import Project
from app.modules.search.schemas import SearchResultItem


async def global_search(db: AsyncSession, query: str, limit: int = 10) -> list[SearchResultItem]:
    like = f"%{query}%"
    results: list[SearchResultItem] = []

    project_rows = (
        await db.execute(select(Project).where(Project.name.ilike(like)).limit(limit))
    ).scalars().all()
    results += [SearchResultItem(id=p.id, type="project", title=p.name, subtitle=p.code) for p in project_rows]

    dataset_rows = (
        await db.execute(select(Dataset).where(Dataset.name.ilike(like)).limit(limit))
    ).scalars().all()
    results += [SearchResultItem(id=d.id, type="dataset", title=d.name, subtitle=d.code) for d in dataset_rows]

    task_rows = (
        await db.execute(select(AnnotationTask).where(AnnotationTask.name.ilike(like)).limit(limit))
    ).scalars().all()
    results += [SearchResultItem(id=t.id, type="annotation_task", title=t.name, subtitle=t.annotation_type.value) for t in task_rows]

    return results
