from fastapi import APIRouter, Depends

from app.agents.k8s.sync import list_pods
from app.api.deps import require_permission
from app.db.session import User

router = APIRouter(prefix="/workloads", tags=["workloads"])


@router.get("/pods")
def get_pods(
    namespace: str | None = None,
    _: User = Depends(require_permission("workload:read")),
):
    pods = list_pods(namespace=namespace)
    return {"items": [p.__dict__ for p in pods], "count": len(pods)}
