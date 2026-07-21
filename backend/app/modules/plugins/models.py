from sqlalchemy import Column, String

from app.core.database import Base
from app.core.mixins import ActiveMixin, TimestampMixin, UUIDMixin


class Plugin(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "plugins"
    __table_args__ = {"schema": "plugins"}

    name = Column(String(150), unique=True, nullable=False)
    version = Column(String(30), nullable=False, default="0.1.0")
    description = Column(String(1000), nullable=True)
