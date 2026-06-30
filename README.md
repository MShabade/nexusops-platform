# NexusOps

**Multi-cloud Kubernetes control plane** — one administrative interface for cluster operations, access governance, incident measurement, and cloud cost visibility.

**Stack:** FastAPI · React · MongoDB · Kubernetes API

---

## Vision

Enterprises should operate Kubernetes the way they operate other critical infrastructure: through a governed control plane with clear roles, measurable reliability, and attributable cost — not through ad hoc CLI access and disconnected cloud consoles.

NexusOps is built to become the standard administrative layer for teams running Kubernetes across AWS EKS, Azure AKS, Google GKE, and on-premises clusters. The intended outcome is reduced operational friction, faster incident response, controlled access for every persona, and FinOps visibility tied directly to running workloads.

---

## What NexusOps is

NexusOps is an enterprise management platform composed of two primary surfaces:

**Administrative Console (React)**  
A browser-based interface for platform engineers, developers, SREs, and finance users. Users interact with clusters, workloads, incidents, and billing through role-appropriate views — not through kubectl or multiple cloud portals.

**Control API (FastAPI)**  
The authoritative backend for authentication, authorization, cluster registry, workload orchestration, incident lifecycle, billing synchronization, and audit. All console actions and external integrations flow through this API. OpenAPI documentation is served at `/docs`.

Behind the API, specialized agents connect to Kubernetes API servers, observability systems, and cloud billing endpoints. Platform state is persisted in MongoDB.

---

## How it behaves

**Cluster registration**  
A platform administrator registers each Kubernetes cluster with provider metadata (AWS, Azure, GCP, on-prem), region, and API endpoint. Registered clusters appear in the central registry. Health and status are evaluated on demand.

**Governed access**  
Every API request is authenticated with JWT and authorized against the caller's role. A developer can operate within assigned namespaces. An SRE can manage incidents and remediation. A FinOps viewer sees cost data only. An auditor has read-only access across the platform with full audit history. Mutating actions are rejected when permissions are insufficient.

**Day-two operations**  
Authorized users scale deployments, trigger rollout restarts, and retrieve pod logs through the API or console. Each action is recorded in the audit log with actor, resource, and timestamp.

**Incident lifecycle**  
When a failure occurs, an incident is created manually or via Alertmanager webhook. The platform captures detection and resolution timestamps. MTTD (Mean Time To Detect) measures how quickly the issue was identified. MTTR (Mean Time To Repair) measures how quickly service was restored after detection. Summary metrics are available per cluster, service, and time window.

**Cost synchronization**  
The billing agent pulls spend from cloud provider APIs on a schedule or on demand. Costs are attributed to cluster, team, and environment using provider tags. Finance and platform teams review summaries without accessing operational controls.

**Audit by default**  
Any change to platform or workload state produces an audit record. This supports post-incident review, compliance, and accountability across distributed teams.

---

## Intended outcomes

- **For platform teams:** one registry and one API for every cluster, regardless of cloud  
- **For developers:** self-service workload operations within namespace boundaries  
- **For SRE:** structured incidents with MTTD and MTTR trends, not unstructured chat triage  
- **For finance:** cloud spend mapped to teams and clusters, not orphaned billing lines  
- **For leadership:** a single platform story — operations, reliability, and cost in one place  

---

## Current status

Phase 1 is in active development. The control API foundation — authentication, RBAC, cluster registry, incident module, billing agent framework, and K8s integration layer — is being built and validated against the architecture described above.

The administrative console and production-grade SSO integration follow in later phases.

---

## Upcoming enhancements

**Near term**  
- MongoDB-backed persistence for users, clusters, incidents, and audit events  
- JWT authentication and six-role RBAC enforcement on all routes  
- Cluster registry with multi-provider support  
- K8s agent: list and operate on pods and deployments  
- Incident API with MTTD / MTTR calculation and summary endpoint  

**Mid term**  
- Alertmanager webhook for automated incident creation and reduced MTTD  
- Billing agent integration with AWS, Azure, and GCP cost APIs  
- Docker Compose stack for local API and MongoDB deployment  
- Integration and API tests  

**Long term**  
- React administrative console (cluster tree, workloads, incidents, FinOps)  
- SSO via OIDC / SAML for enterprise identity providers  
- Helm chart for platform deployment on Kubernetes  
- Agent-based connectivity for private clusters  

---

## Architecture

```
Console (React)
      │  HTTPS / REST
      ▼
Control API (FastAPI) ──► MongoDB
      │
      ├── K8s Agent ──────► EKS · AKS · GKE · on-prem
      ├── Incident Agent ─► Alertmanager / Prometheus
      └── Billing Agent ──► AWS · Azure · GCP billing APIs
```

---

## Technology

- Python 3.11+, FastAPI, Pydantic  
- MongoDB 6.0+  
- React, TypeScript  
- Kubernetes Python client  
- Prometheus, Alertmanager  
- AWS, Azure, GCP billing SDKs  
- Docker  

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
