from app.core.generic_crud import GenericCRUDRouter
from app.modules.experiments.models import Experiment
from app.modules.experiments.schemas import ExperimentCreate, ExperimentRead

router = GenericCRUDRouter(
    model=Experiment,
    read_schema=ExperimentRead,
    create_schema=ExperimentCreate,
    prefix="/experiments",
    tags=["experiments"],
).router
