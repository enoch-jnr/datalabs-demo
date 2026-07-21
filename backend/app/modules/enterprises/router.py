from app.core.generic_crud import GenericCRUDRouter
from app.modules.enterprises.models import Enterprise
from app.modules.enterprises.schemas import EnterpriseCreate, EnterpriseRead

router = GenericCRUDRouter(
    model=Enterprise,
    read_schema=EnterpriseRead,
    create_schema=EnterpriseCreate,
    prefix="/enterprises",
    tags=["enterprises"],
).router
