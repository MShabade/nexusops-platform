# NexusOps

**A new enterprise platform for Kubernetes** — one-click multi-cloud operations, governed access, incident intelligence, and FinOps in a single administrative experience.

**Stack:** FastAPI · React · MongoDB · Kubernetes API

---

## Vision

Kubernetes changed how applications run. It did not change how most organizations operate them. Teams still juggle cloud consoles, CLI tools, spreadsheets for cost, and chat threads for incidents. NexusOps is a new category of platform — an enterprise administrative control plane for Kubernetes — designed to replace that fragmentation with one governed, measurable, one-click experience across every cluster.

We are not wrapping kubectl. We are not assembling buzzword dashboards for demos. NexusOps is a purpose-built product: register a cluster, operate workloads, respond to incidents, and understand spend — from one console, with one access model, on every cloud.

---

## What we are building

NexusOps is a unified management platform for organizations that run Kubernetes at scale across AWS EKS, Azure AKS, Google GKE, and on-premises infrastructure.

**Administrative Console**  
A browser-based interface where authorized users complete operational tasks in one action — register clusters, deploy workloads, scale services, restart deployments, open logs, review incidents, and inspect cloud spend — without switching tools or writing commands.

**Control API**  
The secure backend that powers the console and external integrations. Authentication, authorization, cluster registry, workload orchestration, incident lifecycle, billing synchronization, and audit all flow through a versioned REST API with OpenAPI documentation at `/docs`.

**Intelligent agents**  
Dedicated components connect to Kubernetes API servers, observability systems, and cloud billing endpoints. Platform state lives in MongoDB — built for flexible multi-cloud metadata, incident records, and cost attribution at scale.

---

## One-click operations

NexusOps is designed around operational simplicity. Complex multi-step workflows are reduced to single actions in the console:

- **Register a cluster** — connect EKS, AKS, GKE, or on-prem in one flow  
- **Deploy a workload** — select cluster, namespace, and manifest or Helm release  
- **Scale a service** — adjust replica count without editing YAML on the CLI  
- **Restart a deployment** — rollout restart from one button  
- **View logs** — stream pod output from the workload view  
- **Open an incident** — capture failure context and start the MTTD clock  
- **Resolve and measure** — close the incident and record MTTR automatically  
- **Sync billing** — pull multi-cloud spend and attribute by team or environment  
- **Audit any action** — every click and API call is traceable to a user and timestamp  

The goal is enterprise-grade power with consumer-grade simplicity — the same principle that made administrative consoles the standard for managing complex systems, applied to modern Kubernetes.

---

## How the platform behaves

**Unified multi-cloud registry**  
All clusters appear in one inventory regardless of provider. Platform administrators control registration. Health and metadata are visible from a single view.

**Role-based governance**  
Six roles — Platform Administrator, Cluster Administrator, Developer, SRE, FinOps Viewer, Auditor — each see and do only what their function requires. Every request is authenticated and authorized before execution.

**Incident intelligence**  
Incidents move through a defined lifecycle. The platform measures MTTD (Mean Time To Detect) from failure onset to detection, and MTTR (Mean Time To Repair) from detection to resolution. Metrics aggregate by cluster, service, and period — giving SRE and leadership concrete reliability data, not anecdotal war stories.

**FinOps integration**  
Cloud billing data synchronizes from provider APIs. Spend maps to cluster, team, and environment. Finance and engineering share one source of truth for cost attribution.

**Audit everywhere**  

No silent changes. Registering a cluster, scaling a deployment, or closing an incident leaves a permanent audit record.

---

## Outcomes

- One platform instead of four cloud consoles and a shared kubeconfig  
- One-click day-two ops instead of CLI runbooks for routine tasks  
- Measured reliability instead of untracked downtime  
- Attributed cloud cost instead of unexplained monthly spikes  
- Governed access instead of cluster-admin for everyone  

---

## Product roadmap

**Now under development**  
Control API with MongoDB persistence, JWT authentication, RBAC, cluster registry, K8s workload agent, incident module with MTTD/MTTR, and billing agent framework.

**Next**  
One-click administrative console (React), Alertmanager-driven incident creation, live AWS/Azure/GCP billing sync, Docker deployment package.

**Future**  

Enterprise SSO (OIDC/SAML), Helm-based platform install, private-cluster agent connectivity.

---

## Architecture

NexusOps follows a layered control-plane model. A single deployment hosts the administrative experience and API. Registered Kubernetes clusters and cloud services remain external — connected through agents, not by installing platform software on every cluster.

### System context

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         Enterprise users                                 │
│   Platform Admin · Cluster Admin · Developer · SRE · FinOps · Auditor   │
└─────────────────────────────────┬───────────────────────────────────────┘
                                  │
                    Browser / API clients
                                  │
┌─────────────────────────────────▼───────────────────────────────────────┐
│                         NEXUSOPS CONTROL PLANE                           │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐               │
│  │  Console     │───►│  Control API │───►│   MongoDB    │               │
│  │  (React)     │    │  (FastAPI)   │    │  (platform   │               │
│  │  one-click   │    │  JWT · RBAC  │    │   state)     │               │
│  └──────────────┘    └──────┬───────┘    └──────────────┘               │
│                             │                                            │
│              ┌──────────────┼──────────────┐                            │
│              ▼              ▼              ▼                            │
│        ┌──────────┐  ┌──────────┐  ┌──────────┐                          │
│        │ K8s      │  │ Incident │  │ Billing  │                          │
│        │ Agent    │  │ Agent    │  │ Agent    │                          │
│        └────┬─────┘  └────┬─────┘  └────┬─────┘                          │
└─────────────┼─────────────┼─────────────┼────────────────────────────────┘
              │             │             │
    ┌─────────▼───┐   ┌─────▼─────┐  ┌────▼─────┐
    │ Kubernetes  │   │ Prometheus│  │ AWS ·    │
    │ clusters    │   │ Alertmgr  │  │ Azure ·  │
    │ EKS/AKS/GKE │   │           │  │ GCP APIs │
    │ on-prem     │   │           │  │          │
    └─────────────┘   └───────────┘  └──────────┘
```

### Layer 1 — Presentation (Administrative Console)

The React console is the primary interaction surface. It renders role-specific navigation: cluster inventory, namespace tree, workload detail, incident board, FinOps dashboards, and audit history.

One-click actions in the console map to single API calls. The console holds no cluster credentials. It operates exclusively through the Control API using the authenticated user's JWT.

### Layer 2 — Control API (FastAPI)

The API is the single entry point for all platform behavior. Responsibilities include:

- **Authentication** — JWT issuance and validation on every protected route  
- **Authorization** — role and permission checks before any agent or database operation  
- **Orchestration** — routes one-click requests to the correct agent or persistence layer  
- **Audit** — writes an immutable record for every mutating operation  
- **Versioning** — all endpoints under `/api/v1` with OpenAPI spec at `/docs`  

Internal modules: auth, cluster registry, workload operations, incident management, billing, audit.

### Layer 3 — Agents

Agents encapsulate integration with external systems. Each agent is invoked by the Control API and returns normalized results for storage or direct response.

**K8s Agent**  
Connects to registered cluster API servers using kubeconfig or cloud IAM credentials stored securely per cluster. Performs read operations (pods, deployments, services, nodes, events) and write operations (scale, rollout restart, log stream). Supports EKS, AKS, GKE, and on-premises Kubernetes.

**Incident Agent**  
Manages the incident lifecycle. Accepts manual creation from the console or automated ingestion from Alertmanager webhooks. Computes MTTD and MTTR from timestamped state transitions. Produces aggregated reliability metrics for the summary API.

**Billing Agent**  
Synchronizes cost data from AWS Cost Explorer, Azure Cost Management, and GCP Cloud Billing. Normalizes spend into platform documents tagged by cluster, team, and environment. Triggered on schedule or on demand via one-click sync.

### Layer 4 — Data (MongoDB)

MongoDB holds all platform state as documents:

- **users** — identity, role, credentials  
- **clusters** — registration metadata, provider, endpoint, connection config  
- **incidents** — lifecycle, timestamps, severity, MTTD/MTTR fields  
- **cost_snapshots** — billing periods, amounts, attribution tags  
- **audit_events** — actor, action, resource, timestamp  

Document storage supports heterogeneous alert payloads, evolving cloud tag schemas, and multi-cloud cluster metadata without schema migration overhead.

### Request lifecycle (one-click action)

```
User clicks "Restart deployment"
        │
        ▼
Console sends POST /api/v1/workloads/restart  +  JWT
        │
        ▼
Control API validates token → checks RBAC (workload:write)
        │
        ▼
Audit record created (pending)
        │
        ▼
K8s Agent calls target cluster API → rollout restart
        │
        ▼
Result returned to console + audit record finalized
```

The same pattern applies to cluster registration, incident resolution, and billing sync — authenticate, authorize, audit, execute, respond.

### Multi-cluster topology

NexusOps deploys as a **central control plane**. Member clusters do not require NexusOps software installed locally for standard operation.

- **Control plane** — one NexusOps deployment (API + MongoDB + Console)  
- **Member clusters** — registered by platform admin; accessed via K8s Agent  
- **Connection** — direct API access to cluster endpoint, or private-cluster agent (roadmap)  
- **Isolation** — RBAC scopes users to assigned clusters and namespaces  

This model supports heterogeneous environments: production on EKS, analytics on AKS, legacy on-prem — all visible from one inventory.

### Security architecture

- JWT-based authentication; tokens carry role claims  
- Permission enforcement at API layer before agent invocation  
- Cluster credentials encrypted at rest; never exposed to console client  
- Least-privilege roles — no shared cluster-admin kubeconfig for daily users  
- Full audit trail for compliance and post-incident review  

### Deployment topology

```
┌──────────────── Docker / Kubernetes host ────────────────┐
│  nexusops-console (React)     :3000                       │
│  nexusops-api (FastAPI)       :8000                       │
│  mongodb                      :27017                       │
└──────────────────────────────────────────────────────────┘
          │ outbound only
          ▼
   Target K8s API servers + Cloud billing + Alertmanager
```

---

## Technology

Python 3.11+, FastAPI, Pydantic, MongoDB 6.0+, React, TypeScript, Kubernetes Python client, Prometheus, Alertmanager, AWS/Azure/GCP billing SDKs, Docker.

---

## Configuration

```env
APP_NAME=NexusOps
API_PREFIX=/api/v1
SECRET_KEY=<openssl-rand-hex-32>
MONGODB_URI=mongodb://localhost:27017/nexusops
MONGODB_DB=nexusops
```

---

## License

MIT — see [LICENSE](LICENSE)
