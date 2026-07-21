from app.core.generic_crud import GenericCRUDRouter
from app.modules.billing.models import Subscription
from app.modules.billing.schemas import SubscriptionCreate, SubscriptionRead

router = GenericCRUDRouter(
    model=Subscription,
    read_schema=SubscriptionRead,
    create_schema=SubscriptionCreate,
    prefix="/billing/subscriptions",
    tags=["billing"],
).router
