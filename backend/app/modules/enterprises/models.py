from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import JSONB

from app.core.database import Base
from app.core.mixins import ActiveMixin, TimestampMixin, UUIDMixin


class Enterprise(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "enterprises"
    __table_args__ = {"schema": "enterprises"}

    name = Column(String(150), unique=True, nullable=False)
    code = Column(String(100), unique=True, nullable=False)
    industry = Column(String(100), nullable=True)
    settings = Column(JSONB, nullable=False, default=dict)
