from fastapi import APIRouter

from app.api.routes import auth, billing, clusters, incidents, workloads

api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(clusters.router)
api_router.include_router(incidents.router)
api_router.include_router(billing.router)
api_router.include_router(workloads.router)
