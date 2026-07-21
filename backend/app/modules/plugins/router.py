from app.core.generic_crud import GenericCRUDRouter
from app.modules.plugins.models import Plugin
from app.modules.plugins.schemas import PluginCreate, PluginRead

router = GenericCRUDRouter(
    model=Plugin,
    read_schema=PluginRead,
    create_schema=PluginCreate,
    prefix="/plugins",
    tags=["plugins"],
).router
