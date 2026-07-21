from app.core.generic_crud import GenericCRUDRouter
from app.modules.deployments.models import Deployment
from app.modules.deployments.schemas import DeploymentCreate, DeploymentRead

router = GenericCRUDRouter(
    model=Deployment,
    read_schema=DeploymentRead,
    create_schema=DeploymentCreate,
    prefix="/deployments",
    tags=["deployments"],
).router
