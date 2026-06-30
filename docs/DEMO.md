# Demo — Run NexusOps in 5 Minutes

Anyone who clones this repo can run a live API demo in a few minutes.

## What they'll see

- **NexusOps** — multi-cloud Kubernetes management console (in development)
- Live API at http://localhost:8001/docs
- Endpoints: `/health`, `/about`

---

## Prerequisites

- **Python 3.11+** ([python.org](https://www.python.org/downloads/))
- Git

Check Python:

```powershell
python --version
```

---

## Quick demo (Week 1 learning API)

```powershell
git clone https://github.com/YOUR_USERNAME/nexusops-platform.git
cd nexusops-platform/learn/week-01

python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```

Open:

| URL | What it shows |
|-----|----------------|
| http://localhost:8001/health | Product status |
| http://localhost:8001/about | Product info |
| http://localhost:8001/docs | Interactive API (best for demo) |

**Demo script for a call:**

1. Open `/docs`
2. Click `GET /health` → Try it out → Execute
3. Say: *"This is the control plane API for our K8s console — clusters, RBAC, billing, and incidents will plug in here over the next weeks."*

---

## Optional — full reference API (advanced)

The `backend/` folder has more endpoints (auth, clusters, incidents, billing) from early scaffolding.

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

- Docs: http://localhost:8000/docs  
- Login: `admin@nexusops.dev` / `changeme`

Use this only if you want to show the **target product shape**. Week-by-week learning starts in `learn/week-01/`.

---

## Project docs

| Doc | Purpose |
|-----|---------|
| [README.md](../README.md) | Overview |
| [docs/PRODUCT-VISION.md](PRODUCT-VISION.md) | Market / product story |
| [docs/START-HERE.md](START-HERE.md) | Learn + build track |
| [docs/LINKEDIN-PLAYBOOK.md](LINKEDIN-PLAYBOOK.md) | Build in public posts |

---

## Share this repo

Add to your LinkedIn post:

> Live demo: clone the repo → `learn/week-01` → run uvicorn → open `/docs`  
> GitHub: `https://github.com/YOUR_USERNAME/nexusops-platform`

Replace `YOUR_USERNAME` after you publish to GitHub.
