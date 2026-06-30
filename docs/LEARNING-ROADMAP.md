# 12-Week Learning Roadmap

Build NexusOps from zero to pilot-ready. Each week: **concept → practice → merge to backend → LinkedIn post**.

---

## Week 1 — Foundation & vision

**Concept:** Why a K8s console? WebSphere-style control plane. Architecture layers.

**Learn:**
- Kubernetes basics: cluster, node, namespace, pod, deployment
- FastAPI hello world
- Draw 3-box diagram: UI → API → Clusters

**Build:** `learn/week-01/` — minimal FastAPI with `/health`

**Checkpoint:** You can explain NexusOps to a non-technical manager in 2 minutes.

**LinkedIn:** Posts #1–2 (announce + problem statement)

---

## Week 2 — API skeleton

**Concept:** REST API, project structure, config, OpenAPI docs.

**Learn:**
- FastAPI routers, Pydantic models
- Environment variables (`pydantic-settings`)
- API versioning (`/api/v1`)

**Build:** `learn/week-02/` — structured app: `main.py`, `config.py`, `routes/health.py`

**Checkpoint:** `/docs` shows versioned API.

**LinkedIn:** Posts #3–4 (architecture + Python for K8s backends)

---

## Week 3 — Auth & RBAC

**Concept:** Companies need roles. Least privilege.

**Learn:**
- JWT login flow
- Role enum + permission matrix
- FastAPI dependencies (`Depends`)

**Build:** Login, `/me`, `require_permission("cluster:read")`

**Roles:** platform_admin, cluster_admin, developer, sre, finops_viewer, auditor

**Checkpoint:** Developer cannot call admin-only route (403).

**LinkedIn:** Posts #5–6 (RBAC story + enterprise security)

---

## Week 4 — Cluster registry

**Concept:** Multi-cloud = register many clusters, one control plane.

**Learn:**
- Cluster metadata model (name, provider, region, endpoint)
- kubeconfig handling (never commit secrets)
- minikube or kind for local lab

**Build:** `POST /clusters`, `GET /clusters`

**Checkpoint:** 2 clusters in DB (one AWS, one local).

**LinkedIn:** Posts #7–8 (multi-cloud pain + cluster registry demo)

---

## Week 5 — K8s agent: read-only

**Concept:** Python talks to Kubernetes API.

**Learn:**
- `kubernetes` Python client
- `list_pod_for_all_namespaces`, `list_namespaced_deployment`
- Read-only service account in cluster

**Build:** `GET /workloads/pods`, `GET /workloads/deployments`

**Checkpoint:** Real pod list from minikube in API response.

**LinkedIn:** Posts #9–10 (no kubectl for developers + live demo screenshot)

---

## Week 6 — K8s agent: actions

**Concept:** Console actions = scale, restart, logs.

**Learn:**
- `patch_namespaced_deployment` (scale)
- `read_namespaced_pod_log`
- Rollout restart pattern

**Build:** RBAC-gated write endpoints

**Checkpoint:** Restart deployment from API, not kubectl.

**LinkedIn:** Posts #11–12 (day-2 ops from UI + RBAC in action)

---

## Week 7 — Incidents & MTTD/MTTR

**Concept:** SRE metrics. Support → DevOps story.

**Learn:**
- MTTD = detected_at − failure_started_at
- MTTR = resolved_at − detected_at
- Incident lifecycle: open → investigating → resolved

**Build:** Incident CRUD + `/incidents/metrics/summary`

**Checkpoint:** Create incident, resolve it, API returns avg MTTR.

**LinkedIn:** Posts #13–14 (MTTD/MTTR explained + IT support to SRE journey)

---

## Week 8 — Realistic incident detection

**Concept:** Auto-detect beats manual triage.

**Learn:**
- Prometheus + Alertmanager basics
- Webhook payload → create incident
- Lab: deploy failing app (`deploy/lab/crash-loop/`)

**Build:** `POST /incidents/webhook/alertmanager`

**Checkpoint:** Pod crash → alert → incident → MTTD < 2 min in lab.

**LinkedIn:** Posts #15–16 (before/after MTTD + demo video clip)

---

## Week 9 — Billing agent (AWS)

**Concept:** FinOps. Tags map money to teams.

**Learn:**
- AWS Cost Explorer `GetCostAndUsage`
- Cost allocation tags on EKS
- Chargeback vs showback

**Build:** `billing/aws_collector.py` + `POST /billing/sync`

**Checkpoint:** Real or CSV-backed cost by team tag.

**LinkedIn:** Posts #17–18 (cloud bill blindness + FinOps dashboard)

---

## Week 10 — Multi-cloud billing & audit

**Concept:** One billing model for all clouds. Audit for compliance.

**Learn:**
- Normalized `CostRow` schema
- Azure/GCP stubs or CSV import fallback
- Audit log on every mutating API call

**Build:** `billing/aggregator.py`, audit middleware

**Checkpoint:** Summary shows 2+ sources; audit lists who restarted deployment.

**LinkedIn:** Posts #19–20 (multi-cloud cost + GDPR/audit angle for EU)

---

## Week 11 — React console

**Concept:** Product = what users see.

**Learn:**
- Vite + React + TypeScript
- Login, bearer token, TanStack Query
- 3 pages: Clusters, Incidents, Billing

**Build:** `frontend/` wired to local API

**Checkpoint:** Non-technical user can view pods from browser.

**LinkedIn:** Posts #21–22 (UI screenshot + "built for people who hate kubectl")

---

## Week 12 — Pilot package

**Concept:** Ship for market outreach.

**Learn:**
- README demo video (Loom/OBS)
- Docker Compose one-command start
- Pilot checklist for first company

**Build:** Polish, fix bugs, `docs/PILOT-GUIDE.md`

**Checkpoint:** You can run a 15-min demo call with a prospect.

**LinkedIn:** Posts #23–24 (launch + open for pilot partners)

---

## Daily rhythm (optional)

| Day | Activity (30–60 min) |
|-----|----------------------|
| Mon | Read concept + watch 1 short video |
| Tue | Code exercise from week README |
| Wed | Code + test |
| Thu | Fix bugs / ask for review |
| Fri | Merge to `backend/` if stable |
| Sat | LinkedIn post #1 of week |
| Sun | LinkedIn post #2 + plan next week |

---

## Merge rule

When a week is done:

1. Copy tested code from `learn/week-XX/` → `backend/app/`  
2. Update README with new endpoints  
3. Publish both LinkedIn posts  
4. Tag commit: `week-XX-cluster-registry` etc.  

---

Next week starts at: [learn/week-01/README.md](../learn/week-01/README.md)
