# NexusOps Platform

**Enterprise Kubernetes management console** — manage clusters without the command line.

Inspired by the **enterprise admin console** pattern (central browser UI for complex distributed systems), built for **multi-cloud Kubernetes** (EKS, AKS, GKE, on-prem).

---

## Who this is for

Companies whose teams struggle with `kubectl` and YAML. NexusOps gives them:

- One browser console for all clusters  
- Role-based access (ops, developers, SRE, finance)  
- Deploy, scale, restart, logs — click, not commands  
- Incident tracking (MTTD / MTTR)  
- Multi-cloud billing visibility (FinOps)  

---

## Start here (learning + build track)

**New to the project? Read in this order:**

1. **[docs/SETUP-STEP-BY-STEP.md](docs/SETUP-STEP-BY-STEP.md)** — create GitHub repo + Week 1 (**you run every step**)  
2. [docs/START-HERE.md](docs/START-HERE.md) — how we learn and build together  
3. [docs/PRODUCT-VISION.md](docs/PRODUCT-VISION.md) — what we sell to the market  
4. [docs/LEARNING-ROADMAP.md](docs/LEARNING-ROADMAP.md) — 12-week build plan  
5. [docs/LINKEDIN-PLAYBOOK.md](docs/LINKEDIN-PLAYBOOK.md) — weekly posts to grow reach  
6. [learn/week-01/README.md](learn/week-01/README.md) — Week 1 coding exercises  

---

## Tech stack (target)

| Layer | Technology |
|-------|------------|
| Console UI | React + TypeScript |
| Control API | Python + FastAPI |
| Kubernetes | `kubernetes` Python client |
| Multi-cloud | AWS / Azure / GCP SDKs (agents) |
| Database | PostgreSQL (SQLite for local learning) |

---

## Repository layout

```
nexusops-platform/
├── docs/           # Product + learning + LinkedIn guides
├── learn/          # Week-by-week code you build with us
├── backend/        # Production API (grows each week)
├── frontend/       # Console UI (starts ~Week 8)
└── deploy/         # Docker, lab clusters
```

---

## Quick run (after Week 1 setup)

**Ubuntu / WSL:**

```bash
cd learn/week-01
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```

**Windows PowerShell:**

```powershell
cd learn/week-01
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```

Open http://localhost:8000/docs

---

## Build in public

Follow [docs/LINKEDIN-PLAYBOOK.md](docs/LINKEDIN-PLAYBOOK.md) — 2 posts per week while we build. Goal: companies and engineers reach out for multi-cloud K8s console expertise.

---

## License

MIT — product development and portfolio use.
