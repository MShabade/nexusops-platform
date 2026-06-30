# Week 1 — Foundation

**Goal:** Understand *why* we build NexusOps and run your first API line.

**Time:** 3–5 hours this week.

---

## Concepts (read first)

### 1. The market problem

Companies adopted Kubernetes. Most staff did not adopt kubectl.

- Developers want to deploy, not learn 40 CLI flags  
- Support wants incident context, not YAML  
- Managers want cost and audit, not shell access  

**NexusOps = friendly console for all of them.**

### 2. WebSphere-style → Kubernetes

| Old enterprise console | NexusOps |
|------------------------|----------|
| One browser admin UI | Same |
| Manage many servers | Manage many **clusters** |
| Deploy applications | Deploy **workloads** |
| Start / stop | Scale / restart |
| Admin roles | **RBAC** |

You are not copying IBM. You are applying a **proven UX pattern** to K8s.

### 3. Architecture (draw this)

```
[ User browser ]
       ↓
[ React console ]     ← Week 11
       ↓
[ Python FastAPI ]    ← Weeks 2–10
       ↓
[ Agents: K8s | Billing | Incident ]
       ↓
[ EKS | AKS | GKE | on-prem ]
```

---

## Exercise 1 — Draw on paper (30 min)

Draw the diagram above. Label:

- Where **roles** are checked (API layer)  
- Where **MTTD/MTTR** are calculated (incident agent)  
- Where **billing** data comes from (cloud APIs, not K8s API)  

Take a photo → good LinkedIn content for Post #2.

---

## Exercise 2 — Run hello API (1 hour)

### Step 1: Create virtual environment

```powershell
cd C:\Users\User\Projects\nexusops-platform\learn\week-01
python -m venv .venv
.\.venv\Scripts\activate
pip install fastapi uvicorn
```

### Step 2: Read `main.py`

Open `main.py` in this folder. It is intentionally **small** — only `/health`.

### Step 3: Run

```powershell
uvicorn main:app --reload --port 8001
```

Use port **8001** so you don't conflict with `backend/` on 8000.

### Step 4: Test

- Browser: http://localhost:8001/health  
- Docs: http://localhost:8001/docs  

You should see:

```json
{"status": "ok", "product": "NexusOps", "week": 1}
```

---

## Exercise 3 — Your first code change (30 min)

**Task:** Add endpoint `GET /about` returning:

```json
{
  "name": "NexusOps",
  "tagline": "Kubernetes management console for teams who don't want kubectl",
  "version": "0.1.0-week1"
}
```

**Hints:**
- Use `@app.get("/about")`  
- Return a Python `dict`  

**Test:** http://localhost:8001/about

When done, tell me in chat: *"Week 1 — /about done"* and we'll review.

---

## Exercise 4 — LinkedIn (30 min)

1. Open [docs/LINKEDIN-PLAYBOOK.md](../../docs/LINKEDIN-PLAYBOOK.md)  
2. Post **Week 1 Post #1** (Tuesday) — edit "We're" → "I'm" if solo  
3. Schedule **Post #2** for Friday  

---

## Checklist

- [ ] Read PRODUCT-VISION.md  
- [ ] Drew architecture diagram  
- [ ] Ran week-01 API on port 8001  
- [ ] Added `/about` endpoint yourself  
- [ ] Published LinkedIn Post #1  

---

## Next week preview

Week 2: Split code into folders — `config`, `routes`, proper `/api/v1` prefix.

Do **not** jump ahead. Solid Week 1 = clear story for customers and interviewers.

---

## Questions to test your understanding

1. Why is billing **not** fetched from the Kubernetes API?  
2. Name three personas who use NexusOps and what each needs.  
3. What is the difference between NexusOps RBAC and Kubernetes RBAC?  

*(Answers in docs/PRODUCT-VISION.md and Week 3 preview)*
