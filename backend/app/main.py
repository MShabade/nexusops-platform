from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.config import settings
from app.core.security import hash_password
from app.db.session import Role, User, init_db, SessionLocal


def seed_admin() -> None:
    db = SessionLocal()
    try:
        if not db.query(User).filter(User.email == "admin@nexusops.dev").first():
            db.add(
                User(
                    email="admin@nexusops.dev",
                    full_name="Platform Admin",
                    hashed_password=hash_password("changeme"),
                    role=Role.platform_admin,
                )
            )
            db.commit()
    finally:
        db.close()


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    seed_admin()
    yield


app = FastAPI(title=settings.app_name, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.api_prefix)


@app.get("/health")
def health():
    return {"status": "ok", "service": settings.app_name}
