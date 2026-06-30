"""Incident Agent — MTTD and MTTR computation."""

from datetime import datetime

from app.db.session import Incident


def compute_mttd(failure_started_at: datetime | None, detected_at: datetime | None) -> float | None:
    """Mean Time To Detect (seconds): failure → detection."""
    if not failure_started_at or not detected_at:
        return None
    delta = detected_at - failure_started_at
    return max(delta.total_seconds(), 0)


def compute_mttr(detected_at: datetime | None, resolved_at: datetime | None) -> float | None:
    """Mean Time To Repair (seconds): detection → resolution."""
    if not detected_at or not resolved_at:
        return None
    delta = resolved_at - detected_at
    return max(delta.total_seconds(), 0)


def aggregate_metrics(incidents: list[Incident]) -> dict:
    mttd_values = [
        v
        for i in incidents
        if (v := compute_mttd(i.failure_started_at, i.detected_at)) is not None
    ]
    mttr_values = [
        v
        for i in incidents
        if (v := compute_mttr(i.detected_at, i.resolved_at)) is not None
    ]
    return {
        "count": len(incidents),
        "avg_mttd": sum(mttd_values) / len(mttd_values) if mttd_values else None,
        "avg_mttr": sum(mttr_values) / len(mttr_values) if mttr_values else None,
    }
