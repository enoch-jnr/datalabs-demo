from app.core.generic_crud import GenericCRUDRouter
from app.modules.monitoring.models import MonitoringAlert
from app.modules.monitoring.schemas import MonitoringAlertCreate, MonitoringAlertRead

router = GenericCRUDRouter(
    model=MonitoringAlert,
    read_schema=MonitoringAlertRead,
    create_schema=MonitoringAlertCreate,
    prefix="/monitoring/alerts",
    tags=["monitoring"],
).router
