# RBAC Model

NexusOps defines **application roles** mapped to permissions. These sit above Kubernetes RBAC — NexusOps controls who can use the console and which actions they may trigger.

## Roles

| Role | Description |
|------|-------------|
| `platform_admin` | Full access: users, roles, clusters, all agents |
| `cluster_admin` | Manage assigned clusters: deploy, scale, restart, logs |
| `developer` | Deploy and view workloads in assigned namespaces |
| `sre` | Incidents, MTTD/MTTR, runbooks, remediation actions |
| `finops_viewer` | Billing dashboards, budgets, reports (read-only on workloads) |
| `auditor` | Read-only access to all resources + audit logs |

## Permission Matrix

| Permission | platform_admin | cluster_admin | developer | sre | finops_viewer | auditor |
|------------|:--------------:|:-------------:|:---------:|:---:|:-------------:|:-------:|
| `cluster:read` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `cluster:write` | ✓ | ✓ | | | | |
| `workload:read` | ✓ | ✓ | ✓ | ✓ | | ✓ |
| `workload:write` | ✓ | ✓ | ✓ | ✓ | | |
| `incident:read` | ✓ | ✓ | | ✓ | | ✓ |
| `incident:write` | ✓ | ✓ | | ✓ | | |
| `billing:read` | ✓ | | | | ✓ | ✓ |
| `billing:write` | ✓ | | | | | |
| `user:manage` | ✓ | | | | | |
| `audit:read` | ✓ | | | | | ✓ |

## Implementation

- Roles stored on `User.role` (enum)
- `app/core/rbac.py` — `require_permission(permission)` dependency for FastAPI routes
- Namespace/cluster scoping: `User.assigned_clusters`, `User.assigned_namespaces` (future)

## Interview Talking Point

> "We separate platform personas — developers deploy, SRE owns incidents, finance sees cost — without giving everyone cluster-admin kubeconfig. NexusOps enforces least privilege at the control plane."
