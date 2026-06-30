from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.agents.incident.metrics import aggregate_metrics, compute_mttd, compute_mttr
from app.api.deps import log_audit, require_permission
from app.db.session import Incident, IncidentStatus, User, get_db
from app.schemas.incident import IncidentCreate, IncidentMetrics, IncidentOut, IncidentUpdate

router = APIRouter(prefix="/incidents", tags=["incidents"])


def _incident_to_out(incident: Incident) -> IncidentOut:
    data = IncidentOut.model_validate(incident)
    data.mttd_seconds = compute_mttd(incident.failure_started_at, incident.detected_at)
    data.mttr_seconds = compute_mttr(incident.detected_at, incident.resolved_at)
    return data


@router.get("", response_model=list[IncidentOut])
def list_incidents(
    db: Session = Depends(get_db),
    _: User = Depends(require_permission("incident:read")),
):
    incidents = db.query(Incident).order_by(Incident.created_at.desc()).all()
    return [_incident_to_out(i) for i in incidents]


@router.post("", response_model=IncidentOut)
def create_incident(
    body: IncidentCreate,
    db: Session = Depends(get_db),
    user: User = Depends(require_permission("incident:write")),
):
    incident = Incident(
        title=body.title,
        description=body.description,
        severity=body.severity,
        cluster_id=body.cluster_id,
        service_name=body.service_name,
        failure_started_at=body.failure_started_at,
        detected_at=datetime.utcnow(),
    )
    db.add(incident)
    db.commit()
    db.refresh(incident)
    log_audit(db, user, "create", "incident", str(incident.id), incident.title)
    return _incident_to_out(incident)


@router.patch("/{incident_id}", response_model=IncidentOut)
def update_incident(
    incident_id: int,
    body: IncidentUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(require_permission("incident:write")),
):
    incident = db.query(Incident).filter(Incident.id == incident_id).first()
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")

    if body.status is not None:
        incident.status = body.status
        if body.status == IncidentStatus.investigating and incident.assigned_at is None:
            incident.assigned_at = datetime.utcnow()
        if body.status == IncidentStatus.resolved and incident.resolved_at is None:
            incident.resolved_at = datetime.utcnow()

    if body.assignee_id is not None:
        incident.assignee_id = body.assignee_id
        if incident.assigned_at is None:
            incident.assigned_at = datetime.utcnow()

    db.commit()
    db.refresh(incident)
    log_audit(db, user, "update", "incident", str(incident.id), body.status.value if body.status else "")
    return _incident_to_out(incident)


@router.get("/metrics/summary", response_model=IncidentMetrics)
def incident_metrics(
    days: int = 30,
    db: Session = Depends(get_db),
    _: User = Depends(require_permission("incident:read")),
):
    since = datetime.utcnow() - timedelta(days=days)
    incidents = db.query(Incident).filter(Incident.created_at >= since).all()
    agg = aggregate_metrics(incidents)
    return IncidentMetrics(count=agg["count"], avg_mttd_seconds=agg["avg_mttd"], avg_mttr_seconds=agg["avg_mttr"], period_days=days)
