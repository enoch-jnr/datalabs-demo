import enum

from sqlalchemy import Column, Enum, Integer, String

from app.core.database import Base
from app.core.mixins import ActiveMixin, TimestampMixin, UUIDMixin


class RegistryStage(str, enum.Enum):
    DEV = "DEV"
    STAGING = "STAGING"
    PRODUCTION = "PRODUCTION"


class RegistryEntry(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "registry_entries"
    __table_args__ = {"schema": "registry"}

    name = Column(String(150), nullable=False)
    version = Column(Integer, nullable=False, default=1)
    stage = Column(Enum(RegistryStage), nullable=False, default=RegistryStage.DEV)
