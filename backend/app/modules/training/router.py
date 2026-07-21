from app.core.generic_crud import GenericCRUDRouter
from app.modules.training.models import TrainingJob
from app.modules.training.schemas import TrainingJobCreate, TrainingJobRead

router = GenericCRUDRouter(
    model=TrainingJob,
    read_schema=TrainingJobRead,
    create_schema=TrainingJobCreate,
    prefix="/training-jobs",
    tags=["training"],
).router
