from app.core.generic_crud import GenericCRUDRouter
from app.modules.pipelines.models import Pipeline
from app.modules.pipelines.schemas import PipelineCreate, PipelineRead

router = GenericCRUDRouter(
    model=Pipeline,
    read_schema=PipelineRead,
    create_schema=PipelineCreate,
    prefix="/pipelines",
    tags=["pipelines"],
).router
