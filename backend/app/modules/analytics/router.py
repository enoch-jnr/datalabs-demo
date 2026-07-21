from app.core.generic_crud import GenericCRUDRouter
from app.modules.analytics.models import Dashboard
from app.modules.analytics.schemas import DashboardCreate, DashboardRead

router = GenericCRUDRouter(
    model=Dashboard,
    read_schema=DashboardRead,
    create_schema=DashboardCreate,
    prefix="/analytics/dashboards",
    tags=["analytics"],
).router
