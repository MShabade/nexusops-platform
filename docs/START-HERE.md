# Start Here — Learn & Build NexusOps From Scratch

Welcome. We build **NexusOps** step by step: concepts first, then code, then LinkedIn posts so the market finds you.

---

## What we are building

A **WebSphere-style admin console for Kubernetes**:

- Friendly browser UI (no kubectl for daily tasks)  
- Multi-cluster / multi-cloud (AWS, Azure, GCP, on-prem)  
- Roles for platform admin, developer, SRE, FinOps  
- Billing agent + incident agent (MTTD / MTTR)  

**This is a commercial product for companies**, not a thesis.

---

## How we work together

| Step | You | Me (Cursor) |
|------|-----|-------------|
| 1 | Read the **concept** for the week | Explain architecture in plain language |
| 2 | Read **learn/week-XX/** README | Answer questions |
| 3 | **Type the code** yourself in `learn/` | Review, hint, fix errors |
| 4 | Copy **LinkedIn post** from playbook | Help refine your voice |
| 5 | Merge working code into `backend/` when ready | Guide integration |

**Rule:** We do not skip weeks. Each week adds one capability.

---

## Your 12-week journey

| Week | Concept | You build |
|------|---------|-----------|
| 1 | Why console? WebSphere → K8s mapping | Hello FastAPI + architecture diagram |
| 2 | REST API + project structure | API skeleton, health, config |
| 3 | Auth + RBAC | Login, roles, permissions |
| 4 | Cluster registry | Register EKS/minikube cluster |
| 5 | K8s agent — read workloads | List pods, deployments, nodes |
| 6 | K8s agent — actions | Scale, restart, logs (RBAC-gated) |
| 7 | Incident agent + MTTD/MTTR | Create/resolve incidents, metrics |
| 8 | Alert webhook (realistic MTTD) | Alertmanager → incident |
| 9 | Billing agent (AWS first) | Cost by tag/team |
| 10 | Multi-cloud billing + audit log | Azure/GCP or CSV fallback |
| 11 | React console (3 screens) | Clusters, incidents, billing |
| 12 | Demo + pilot package | Video, docs, outreach |

Full detail: [LEARNING-ROADMAP.md](LEARNING-ROADMAP.md)

---

## Folder guide

| Path | Purpose |
|------|---------|
| `learn/week-01/` … `week-12/` | **You code here** while learning |
| `backend/` | Production API — copy from `learn/` when a week is done |
| `docs/` | Concepts, product vision, LinkedIn |
| `frontend/` | React console (Week 11+) |
| `deploy/lab/` | Sample failing app for incident demos |

---

## Week 1 — do this today

1. Read [PRODUCT-VISION.md](PRODUCT-VISION.md) (15 min)  
2. Draw the architecture on paper (cluster → API → console)  
3. Follow [learn/week-01/README.md](../learn/week-01/README.md)  
4. Post **LinkedIn Week 1 Post #1** from [LINKEDIN-PLAYBOOK.md](LINKEDIN-PLAYBOOK.md)  

---

## When you get stuck

Ask in chat with:

- Week number  
- What you tried  
- Error message (if any)  

Example: *"Week 4 — cluster register returns 403, I assigned platform_admin role"*

---

## Success at Week 12

- Runnable console backed by Python API  
- 1+ real cluster connected  
- Incidents with MTTD/MTTR demo  
- Billing view (AWS or CSV)  
- 24 LinkedIn posts published  
- Companies can **request a demo** from your profile  

Next: [PRODUCT-VISION.md](PRODUCT-VISION.md)
