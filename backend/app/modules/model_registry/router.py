from app.core.generic_crud import GenericCRUDRouter
from app.modules.model_registry.models import MLModel
from app.modules.model_registry.schemas import MLModelCreate, MLModelRead

router = GenericCRUDRouter(
    model=MLModel,
    read_schema=MLModelRead,
    create_schema=MLModelCreate,
    prefix="/models",
    tags=["model-registry"],
).router
