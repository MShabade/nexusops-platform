from datetime import datetime

from pydantic import BaseModel


class BillingSummary(BaseModel):
    total_usd: float
    period_start: datetime
    period_end: datetime
    by_cluster: list[dict]
    by_team: list[dict]


class CostSnapshotOut(BaseModel):
    id: int
    cluster_id: int | None
    team: str
    period_start: datetime
    period_end: datetime
    amount_usd: float
    currency: str
    provider: str

    model_config = {"from_attributes": True}
