from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import log_audit, require_permission
from app.db.session import Cluster, User, get_db
from app.schemas.cluster import ClusterCreate, ClusterOut

router = APIRouter(prefix="/clusters", tags=["clusters"])


@router.get("", response_model=list[ClusterOut])
def list_clusters(
    db: Session = Depends(get_db),
    _: User = Depends(require_permission("cluster:read")),
):
    return db.query(Cluster).order_by(Cluster.name).all()


@router.post("", response_model=ClusterOut)
def register_cluster(
    body: ClusterCreate,
    db: Session = Depends(get_db),
    user: User = Depends(require_permission("cluster:write")),
):
    if db.query(Cluster).filter(Cluster.name == body.name).first():
        raise HTTPException(status_code=400, detail="Cluster name already exists")
    cluster = Cluster(**body.model_dump())
    db.add(cluster)
    db.commit()
    db.refresh(cluster)
    log_audit(db, user, "register", "cluster", str(cluster.id), cluster.name)
    return cluster


@router.get("/{cluster_id}", response_model=ClusterOut)
def get_cluster(
    cluster_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(require_permission("cluster:read")),
):
    cluster = db.query(Cluster).filter(Cluster.id == cluster_id).first()
    if not cluster:
        raise HTTPException(status_code=404, detail="Cluster not found")
    return cluster
