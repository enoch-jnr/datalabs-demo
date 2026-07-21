from app.core.generic_crud import GenericCRUDRouter
from app.modules.marketplace.models import MarketplaceItem
from app.modules.marketplace.schemas import MarketplaceItemCreate, MarketplaceItemRead

router = GenericCRUDRouter(
    model=MarketplaceItem,
    read_schema=MarketplaceItemRead,
    create_schema=MarketplaceItemCreate,
    prefix="/marketplace/items",
    tags=["marketplace"],
).router
