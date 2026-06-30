# NexusOps

> **Multi-cloud Kubernetes control plane** — unified cluster operations, RBAC, incident metrics (MTTD/MTTR), FinOps, and audit.  
> **Stack:** FastAPI · React · MongoDB · Kubernetes API

---

## At a glance

| | |
|---|---|
| **Purpose** | Enterprise admin console for Kubernetes across AWS EKS, Azure AKS, Google GKE, on-prem |
| **Control API** | Python 3.11+ / FastAPI — REST, JWT, OpenAPI at `/docs` |
| **Datastore** | MongoDB 6.0+ — users, clusters, incidents, billing, audit |
| **Integrations** | Kubernetes API · Alertmanager · AWS/Azure/GCP Billing |
| **Console** | React / TypeScript administrative UI |

---

## Problem → solution

| Operational gap | NexusOps capability |
|-----------------|---------------------|
| Per-cloud silos | Single registry and UI for all clusters |
| CLI-only day-2 ops | Scale, restart, logs, deploy via API/console |
| No cost attribution | FinOps sync — spend by cluster, team, tag |
| Unmeasured incidents | MTTD / MTTR per cluster, service, window |
| Over-privileged access | Six-role RBAC + immutable audit log |

---

## Architecture

```
Console (React)
      │  HTTPS / REST
      ▼
Control API (FastAPI) ──► MongoDB
      │
      ├── K8s Agent ──────► EKS · AKS · GKE · on-prem API servers
      ├── Incident Agent ─► Alertmanager / Prometheus webhooks
      └── Billing Agent ──► AWS CE · Azure Cost · GCP Billing
```

**Request path:** Console → JWT-validated API → RBAC check → agent or MongoDB → audit entry on mutation.

---

## Technology stack

| Layer | Technology | Notes |
|-------|------------|-------|
| Console | React, TypeScript | Cluster tree, workloads, incidents, FinOps views |
| API | FastAPI, Pydantic | Versioned `/api/v1`, auto OpenAPI |
| Auth | JWT (HS256), OAuth2 password flow | Role embedded in token claims |
| Database | **MongoDB** | Motor (async driver) or PyMongo |
| K8s | `kubernetes` Python client | Per-cluster kubeconfig / IAM |
| Observability | Prometheus, Alertmanager | Webhook → incident creation |
| Billing | boto3, Azure SDK, GCP SDK | Tag-based chargeback |
| Deploy | Docker, Compose | API + MongoDB local stack |

### MongoDB collections

| Collection | Contents |
|------------|----------|
| `users` | Identity, hashed credentials, role |
| `clusters` | Name, provider, region, endpoint, status |
| `incidents` | Lifecycle timestamps, severity, MTTD/MTTR fields |
| `cost_snapshots` | Period, amount, cluster, team, provider |
| `audit_events` | Actor, action, resource, timestamp |

Document model supports evolving alert payloads and multi-cloud tag schemas without relational migrations.

---

## RBAC

| Role | Permissions |
|------|-------------|
| `platform_admin` | Users, clusters, all modules |
| `cluster_admin` | Full ops on assigned clusters |
| `developer` | Read/write workloads in assigned namespaces |
| `sre` | Incidents, remediation, metrics |
| `finops_viewer` | Billing read-only |
| `auditor` | Read-only all + audit log |

Enforced at API layer via permission dependencies on every route.

---

## Reliability metrics

| Metric | Formula | Stored fields |
|--------|---------|---------------|
| **MTTD** | `detected_at − failure_started_at` | ISO timestamps on incident document |
| **MTTR** | `resolved_at − detected_at` | Computed on resolve; aggregated in summary API |

**Summary endpoint:** `GET /api/v1/incidents/metrics/summary?days=30`  
Returns count, `avg_mttd_seconds`, `avg_mttr_seconds` per reporting window.

---

## API reference

Base URL: `http://<host>:8000` · Docs: `/docs` · Health: `/health`

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `POST` | `/api/v1/auth/login` | — | Issue JWT |
| `GET` | `/api/v1/auth/me` | JWT | Current user + role |
| `GET` | `/api/v1/clusters` | `cluster:read` | List clusters |
| `POST` | `/api/v1/clusters` | `cluster:write` | Register cluster |
| `GET` | `/api/v1/workloads/pods` | `workload:read` | List pods (K8s agent) |
| `GET` | `/api/v1/incidents` | `incident:read` | List incidents |
| `PATCH` | `/api/v1/incidents/{id}` | `incident:write` | Update status / assignee |
| `GET` | `/api/v1/incidents/metrics/summary` | `incident:read` | MTTD / MTTR aggregates |
| `GET` | `/api/v1/billing/summary` | `billing:read` | Cost by cluster / team |
| `POST` | `/api/v1/billing/sync` | `billing:write` | Trigger billing agent |

**Authentication header:** `Authorization: Bearer <token>`

---

## Configuration

```env
# Application
APP_NAME=NexusOps
API_PREFIX=/api/v1
SECRET_KEY=<openssl rand -hex 32>
CORS_ORIGINS=["http://localhost:3000"]

# MongoDB
MONGODB_URI=mongodb://localhost:27017/nexusops
MONGODB_DB=nexusops

# Optional — billing agents
AWS_DEFAULT_REGION=eu-west-1
# AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY via IAM role or env
```

| Variable | Required | Description |
|----------|----------|-------------|
| `MONGODB_URI` | Yes | MongoDB connection string |
| `SECRET_KEY` | Yes | JWT signing key |
| `API_PREFIX` | No | Default `/api/v1` |
| `CORS_ORIGINS` | No | JSON array of allowed origins |

---

## System requirements

| Component | Minimum |
|-----------|---------|
| Python | 3.11 |
| MongoDB | 6.0 |
| Memory (API) | 512 MB |
| Memory (MongoDB) | 1 GB (dev) |
| Network | Outbound to target K8s API servers and cloud billing endpoints |

**Supported Kubernetes distributions:** EKS, AKS, GKE, Rancher RKE, upstream Kubernetes 1.26+.

---

## Delivery roadmap

| Phase | Scope | Status |
|-------|-------|--------|
| 1 | Control API, MongoDB, JWT, RBAC | In progress |
| 2 | Cluster registry, K8s agent (read/write) | Planned |
| 3 | Incidents, Alertmanager webhook, MTTD/MTTR | Planned |
| 4 | Billing agent, FinOps API | Planned |
| 5 | React console, SSO (OIDC/SAML) | Planned |

---

## License

MIT — see [LICENSE](LICENSE)
