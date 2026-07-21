from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import get_current_active_user
from app.modules.core.models import User
from app.modules.search import service
from app.modules.search.schemas import SearchResponse

router = APIRouter(prefix="/search", tags=["search"])


@router.get("/", response_model=SearchResponse)
async def search(
    q: str,
    db: AsyncSession = Depends(get_db),
    _current_user: User = Depends(get_current_active_user),
):
    """
    Real ILIKE-based search across projects, datasets, and annotation
    tasks. Good enough for a demo; swap for the `search` module's own
    SearchIndex/Elasticsearch-backed implementation as usage grows.
    """
    results = await service.global_search(db, q)
    return SearchResponse(query=q, results=results)
