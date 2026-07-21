from app.core.generic_crud import GenericCRUDRouter
from app.modules.audit.models import AuditLog
from app.modules.audit.schemas import AuditLogCreate, AuditLogRead

router = GenericCRUDRouter(
    model=AuditLog,
    read_schema=AuditLogRead,
    create_schema=AuditLogCreate,
    prefix="/audit/logs",
    tags=["audit"],
).router
