import uuid
from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime
from sqlalchemy.dialects.postgresql import UUID


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class UUIDMixin:
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )


class TimestampMixin:
    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=utcnow,
    )

    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=utcnow,
        onupdate=utcnow,
    )


class ActiveMixin:
    is_active = Column(
        Boolean,
        nullable=False,
        default=True,
    )
