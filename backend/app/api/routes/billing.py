from datetime import datetime, timedelta

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.agents.billing.collector import sync_billing
from app.api.deps import log_audit, require_permission
from app.db.session import CostSnapshot, User, get_db
from app.schemas.billing import BillingSummary, CostSnapshotOut

router = APIRouter(prefix="/billing", tags=["billing"])


@router.get("/summary", response_model=BillingSummary)
def billing_summary(
    days: int = 30,
    db: Session = Depends(get_db),
    _: User = Depends(require_permission("billing:read")),
):
    since = datetime.utcnow() - timedelta(days=days)
    rows = db.query(CostSnapshot).filter(CostSnapshot.period_start >= since).all()
    total = sum(r.amount_usd for r in rows)

    by_cluster: dict[int | None, float] = {}
    by_team: dict[str, float] = {}
    for r in rows:
        by_cluster[r.cluster_id] = by_cluster.get(r.cluster_id, 0) + r.amount_usd
        by_team[r.team] = by_team.get(r.team, 0) + r.amount_usd

    return BillingSummary(
        total_usd=round(total, 2),
        period_start=since,
        period_end=datetime.utcnow(),
        by_cluster=[{"cluster_id": k, "amount_usd": round(v, 2)} for k, v in by_cluster.items()],
        by_team=[{"team": k, "amount_usd": round(v, 2)} for k, v in by_team.items()],
    )


@router.get("/snapshots", response_model=list[CostSnapshotOut])
def list_snapshots(
    db: Session = Depends(get_db),
    _: User = Depends(require_permission("billing:read")),
):
    return db.query(CostSnapshot).order_by(CostSnapshot.period_start.desc()).limit(100).all()


@router.post("/sync")
def trigger_billing_sync(
    db: Session = Depends(get_db),
    user: User = Depends(require_permission("billing:write")),
):
    inserted = sync_billing(db)
    log_audit(db, user, "sync", "billing", "", f"{inserted} snapshots")
    return {"status": "ok", "inserted": inserted}
