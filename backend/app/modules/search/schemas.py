import uuid

from pydantic import BaseModel


class SearchResultItem(BaseModel):
    id: uuid.UUID
    type: str
    title: str
    subtitle: str | None = None


class SearchResponse(BaseModel):
    query: str
    results: list[SearchResultItem]
