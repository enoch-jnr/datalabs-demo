from app.core.generic_crud import GenericCRUDRouter
from app.modules.inference.models import InferenceRequest
from app.modules.inference.schemas import InferenceRequestCreate, InferenceRequestRead

router = GenericCRUDRouter(
    model=InferenceRequest,
    read_schema=InferenceRequestRead,
    create_schema=InferenceRequestCreate,
    prefix="/inference",
    tags=["inference"],
).router
