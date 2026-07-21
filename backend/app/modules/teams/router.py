from app.core.generic_crud import GenericCRUDRouter
from app.modules.teams.models import Team
from app.modules.teams.schemas import TeamCreate, TeamRead

router = GenericCRUDRouter(
    model=Team,
    read_schema=TeamRead,
    create_schema=TeamCreate,
    prefix="/teams",
    tags=["teams"],
).router
