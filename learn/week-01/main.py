"""
NexusOps — Week 1 learning API

This is intentionally minimal. You run and extend it yourself.

Week 1 tasks:
  1. Run: uvicorn main:app --reload --port 8001
  2. Visit: http://localhost:8001/docs
  3. Add GET /about (see learn/week-01/README.md)

Do not copy from backend/ yet — learn by typing.
"""

from fastapi import FastAPI

app = FastAPI(
    title="NexusOps",
    description="Week 1 — Kubernetes management console (learning track)",
    version="0.1.0-week1",
)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "product": "NexusOps",
        "week": 1,
        "message": "Enterprise K8s console — learn & build track",
    }


@app.get("/about")
def about():
    return {
        "name": "NexusOps",
        "tagline": "Kubernetes management console for teams who don't want kubectl",
        "version": "0.1.0-week1",
        "repo": "https://github.com/YOUR_USERNAME/nexusops-platform",
        "demo": "Run learn/week-01 and open /docs",
    }


# Customize tagline and repo URL above, then commit to GitHub.
