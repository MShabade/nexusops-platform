# NexusOps

**Multi-cloud Kubernetes control plane** for enterprise cluster operations, access governance, incident metrics, and FinOps.

NexusOps delivers a unified administrative console and REST API to manage Kubernetes across AWS EKS, Azure AKS, Google GKE, and on-premises environments. Platform teams gain a single interface for day-two operations, role-based access, reliability measurement, and cloud cost visibility — without routing every request through kubectl.

**Stack:** FastAPI · React · MongoDB · Kubernetes API

---

## Overview

Organizations running Kubernetes at scale typically operate across multiple cloud providers, each with its own console, credential model, and cost reporting. Operational tasks fall to a small group comfortable with CLI workflows. Incident detection and recovery times are rarely measured consistently. Finance lacks clear attribution between cloud spend and running workloads.

NexusOps addresses this by consolidating cluster management into one control plane. The platform registers heterogeneous clusters, enforces least-privilege access by role, exposes workload operations through a documented API, tracks MTTD and MTTR through structured incidents, and synchronizes billing data for chargeback and reporting.

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
      └── Billing Agent ──► AWS · Azure · GCP billing APIs
```

Incoming requests are authenticated via JWT, authorized against role permissions, executed through the appropriate agent or persisted to MongoDB, and recorded in the audit log when mutating state.

The administrative console consumes the same API used by automation and integrators. OpenAPI documentation is available at `/docs` on a running control API instance.

---

## Core capabilities

**Multi-cluster management**  
Register and monitor Kubernetes clusters regardless of provider or region. Central visibility into cluster health, metadata, and namespace-scoped access.

**Workload operations**  
View and control deployments, pods, services, and logs. Scale replicas, trigger rollout restarts, and retrieve log streams through the API or console — authorized per role and namespace.

**Identity and access management**  
Six built-in roles: Platform Administrator, Cluster Administrator, Developer, SRE, FinOps Viewer, and Auditor. Permissions are enforced at the API layer on every endpoint.

**Incident and reliability management**  
Incidents follow a defined lifecycle from detection through resolution. The platform records MTTD (Mean Time To Detect) as the interval between failure onset and detection, and MTTR (Mean Time To Repair) as the interval between detection and resolution. Metrics aggregate by cluster, service, and reporting window via `/api/v1/incidents/metrics/summary`.

**FinOps**  
The billing agent synchronizes cost data from cloud provider APIs. Spend is mapped to cluster, team, and environment using provider tags and labels, surfaced through the billing summary API.

**Audit**  
All mutating operations produce an audit record: actor, action, resource, and timestamp.

---

## Technology

- **Console:** React, TypeScript  
- **Control API:** Python 3.11+, FastAPI, Pydantic  
- **Datastore:** MongoDB 6.0+ (users, clusters, incidents, cost snapshots, audit events)  
- **Cluster integration:** Official Kubernetes Python client  
- **Observability:** Prometheus, Alertmanager webhook ingestion  
- **Billing:** AWS Cost Explorer, Azure Cost Management, GCP Cloud Billing  
- **Deployment:** Docker, Docker Compose  

MongoDB provides document storage for platform metadata, incident payloads, and multi-cloud tagging models without rigid schema migrations.

---

## API

Base URL: `http://<host>:8000`  
Health: `GET /health`  
Documentation: `GET /docs`

Authenticated routes require `Authorization: Bearer <token>`.

**Authentication**  
`POST /api/v1/auth/login` — issue JWT  
`GET /api/v1/auth/me` — current user and role  

**Clusters**  
`GET /api/v1/clusters` — list registered clusters  
`POST /api/v1/clusters` — register a cluster  

**Workloads**  
`GET /api/v1/workloads/pods` — list pods via K8s agent  

**Incidents**  
`GET /api/v1/incidents` — list incidents  
`PATCH /api/v1/incidents/{id}` — update status or assignee  
`GET /api/v1/incidents/metrics/summary` — MTTD / MTTR aggregates  

**Billing**  
`GET /api/v1/billing/summary` — cost by cluster and team  
`POST /api/v1/billing/sync` — trigger billing synchronization  

---

## Configuration

```env
APP_NAME=NexusOps
API_PREFIX=/api/v1
SECRET_KEY=<generate-with-openssl-rand-hex-32>
CORS_ORIGINS=["http://localhost:3000"]

MONGODB_URI=mongodb://localhost:27017/nexusops
MONGODB_DB=nexusops
```

`MONGODB_URI` and `SECRET_KEY` are required. Remaining variables have sensible defaults for local deployment.

---

## Requirements

- Python 3.11 or later  
- MongoDB 6.0 or later  
- Outbound network access to target Kubernetes API endpoints  
- Optional: Docker 24+ for containerized deployment  

Supported distributions include EKS, AKS, GKE, Rancher RKE, and upstream Kubernetes 1.26+.

---

## Roadmap

**Phase 1** — Control API, MongoDB persistence, JWT authentication, RBAC  
**Phase 2** — Cluster registry, K8s agent (read and write workloads)  
**Phase 3** — Incident module, Alertmanager integration, MTTD / MTTR reporting  
**Phase 4** — Billing agent, multi-cloud FinOps API  
**Phase 5** — Administrative console, SSO (OIDC / SAML)  

Phase 1 is in active development.

---

## License

MIT — see [LICENSE](LICENSE)
