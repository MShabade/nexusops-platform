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

**Building the full industry app side-by-side? Start here:**

1. **[docs/FULL-APP-GUIDE.md](docs/FULL-APP-GUIDE.md)** — learn in `learn/`, peek `reference/`, merge to `app/`  
2. **[docs/DAILY-COMMITS.md](docs/DAILY-COMMITS.md)** — daily tasks + commit messages  
3. **[docs/INDUSTRY-FOLDER-STRUCTURE.md](docs/INDUSTRY-FOLDER-STRUCTURE.md)** — production folder layout  
4. **[docs/SETUP-STEP-BY-STEP.md](docs/SETUP-STEP-BY-STEP.md)** — GitHub + Ubuntu setup  
5. **[learn/week-02/README.md](learn/week-02/README.md)** — **Week 2 Day 1 (start if Week 1 done)**  

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
├── app/              # YOUR production API (merge weekly — starts empty)
├── learn/            # YOU code here each week
├── reference/        # READ-ONLY complete example (compare, don't copy)
├── docs/             # Guides, daily commits, LinkedIn
├── frontend/         # React console (later)
└── deploy/
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
