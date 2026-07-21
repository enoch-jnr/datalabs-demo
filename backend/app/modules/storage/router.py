from app.core.generic_crud import GenericCRUDRouter
from app.modules.storage.models import StorageBucket
from app.modules.storage.schemas import StorageBucketCreate, StorageBucketRead

router = GenericCRUDRouter(
    model=StorageBucket,
    read_schema=StorageBucketRead,
    create_schema=StorageBucketCreate,
    prefix="/storage/buckets",
    tags=["storage"],
).router
