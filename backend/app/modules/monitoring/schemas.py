import uuid

from pydantic import BaseModel, ConfigDict

from app.modules.monitoring.models import AlertSeverity


class MonitoringAlertCreate(BaseModel):
    project_id: uuid.UUID
    name: str
    severity: AlertSeverity = AlertSeverity.LOW
    message: str | None = None


class MonitoringAlertRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    project_id: uuid.UUID
    name: str
    severity: AlertSeverity
    message: str | None
