from datetime import datetime

from pydantic import BaseModel

from app.db.session import IncidentStatus


class IncidentCreate(BaseModel):
    title: str
    description: str = ""
    severity: str = "medium"
    cluster_id: int | None = None
    service_name: str = ""
    failure_started_at: datetime | None = None


class IncidentUpdate(BaseModel):
    status: IncidentStatus | None = None
    assignee_id: int | None = None


class IncidentOut(BaseModel):
    id: int
    title: str
    description: str
    severity: str
    status: IncidentStatus
    cluster_id: int | None
    service_name: str
    failure_started_at: datetime | None
    detected_at: datetime
    assigned_at: datetime | None
    resolved_at: datetime | None
    assignee_id: int | None
    mttd_seconds: float | None = None
    mttr_seconds: float | None = None

    model_config = {"from_attributes": True}


class IncidentMetrics(BaseModel):
    count: int
    avg_mttd_seconds: float | None
    avg_mttr_seconds: float | None
    period_days: int
