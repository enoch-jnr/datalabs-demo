from app.core.generic_crud import GenericCRUDRouter
from app.modules.registry.models import RegistryEntry
from app.modules.registry.schemas import RegistryEntryCreate, RegistryEntryRead

router = GenericCRUDRouter(
    model=RegistryEntry,
    read_schema=RegistryEntryRead,
    create_schema=RegistryEntryCreate,
    prefix="/registry",
    tags=["registry"],
).router
