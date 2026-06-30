"""Billing Agent — FinOps cost collection and chargeback."""

from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.db.session import CostSnapshot


def sync_billing(db: Session, provider: str = "aws") -> int:
    """
    Pull cost data from cloud APIs and persist snapshots.
    MVP: seeds demo data when cloud APIs are not configured.
    Replace `_fetch_cloud_costs` with boto3/Azure/GCP SDK in Phase 3.
    """
    rows = _fetch_cloud_costs(provider)
    for row in rows:
        db.add(
            CostSnapshot(
                cluster_id=row.get("cluster_id"),
                team=row.get("team", "unassigned"),
                period_start=row["period_start"],
                period_end=row["period_end"],
                amount_usd=row["amount_usd"],
                provider=provider,
            )
        )
    db.commit()
    return len(rows)


def _fetch_cloud_costs(provider: str) -> list[dict]:
    """Demo data for development; swap for real Cost Explorer / Azure / GCP calls."""
    now = datetime.utcnow()
    start = now - timedelta(days=30)
    return [
        {
            "cluster_id": 1,
            "team": "platform",
            "period_start": start,
            "period_end": now,
            "amount_usd": 842.50,
        },
        {
            "cluster_id": 1,
            "team": "product-a",
            "period_start": start,
            "period_end": now,
            "amount_usd": 1203.75,
        },
        {
            "cluster_id": 2,
            "team": "product-b",
            "period_start": start,
            "period_end": now,
            "amount_usd": 567.20,
        },
    ]
