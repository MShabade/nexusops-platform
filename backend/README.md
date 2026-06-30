# Reference implementation (read-only for now)

This folder contains early NexusOps API code created during initial scaffolding.

**Learning rule:** Build in `learn/week-XX/` first. Compare here when stuck — do not copy blindly.

When your week passes tests, we merge your code here together.

## What's already here (preview of final product)

- FastAPI app with `/api/v1` routes  
- RBAC roles and permissions  
- Cluster, incident, billing endpoints  
- Agents: k8s, billing, incident  

## Run reference API (optional peek)

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Login: `admin@nexusops.dev` / `changeme`

**Your path:** Start at `learn/week-01/` instead if learning from scratch.
