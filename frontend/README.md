# NexusOps Web Console (React)

The browser UI for NexusOps — cluster tree, workloads, incidents, billing dashboards.

## Planned screens

| Screen | Role access |
|--------|-------------|
| Login | All |
| Cluster overview | cluster:read |
| Workloads (pods, deployments) | workload:read |
| Incidents + MTTD/MTTR dashboard | incident:read |
| Billing / FinOps | billing:read |
| Users & roles | user:manage |
| Audit log | audit:read |

## Stack (Phase 4)

- React + TypeScript + Vite
- TanStack Query for API calls
- Recharts for billing and incident metrics

## API base URL

```
http://localhost:8000/api/v1
```

Scaffold with:

```bash
npm create vite@latest . -- --template react-ts
npm install axios @tanstack/react-query recharts
```

Backend is ready — connect to `/auth/login`, `/clusters`, `/incidents`, `/billing`.
