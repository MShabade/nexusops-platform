# Step-by-Step — Create GitHub Repo & Share Demo

Follow these steps once on your machine. After that, anyone can clone and run the demo.

---

## Part A — You: publish to GitHub (15 minutes)

### Step 1 — Open project in terminal

```powershell
cd C:\Users\User\Projects\nexusops-platform
```

### Step 2 — Verify git (already initialized)

```powershell
git status
```

You should see tracked/untracked files. If `git` is not found, install [Git for Windows](https://git-scm.com/download/win).

### Step 3 — First commit (local)

```powershell
git add .
git commit -m "Initial commit: NexusOps platform scaffold, Week 1 demo API, docs"
```

### Step 4 — Create empty repo on GitHub

1. Go to https://github.com/new  
2. **Repository name:** `nexusops-platform`  
3. **Description:** `Multi-cloud Kubernetes management console — enterprise-style admin UI for K8s`  
4. Choose **Public** (so anyone can clone for demo)  
5. **Do NOT** add README, .gitignore, or license (we already have them)  
6. Click **Create repository**

### Step 5 — Push your code

GitHub shows commands — use these (replace `YOUR_USERNAME`):

```powershell
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/nexusops-platform.git
git push -u origin main
```

Sign in when prompted (browser or token).

### Step 6 — Test the link

Open `https://github.com/YOUR_USERNAME/nexusops-platform` — README should display.

---

## Part B — Anyone: run the demo (5 minutes)

Share this with prospects, colleagues, or LinkedIn:

```powershell
git clone https://github.com/YOUR_USERNAME/nexusops-platform.git
cd nexusops-platform/learn/week-01
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```

Then open: **http://localhost:8001/docs**

Full details: [docs/DEMO.md](DEMO.md)

---

## Part C — You: start Week 1 learning (2–3 hours)

### Day 1 checklist

- [ ] Repo pushed to GitHub  
- [ ] Run demo locally (Part B)  
- [ ] Read `docs/PRODUCT-VISION.md` (20 min)  
- [ ] Draw architecture diagram on paper (30 min)  
- [ ] Post LinkedIn Week 1 Post #1 from `docs/LINKEDIN-PLAYBOOK.md`  

### Day 2 checklist

- [ ] Customize `GET /about` in `learn/week-01/main.py` (add your tagline if you want)  
- [ ] Commit and push: `git add . && git commit -m "Week 1: customize about endpoint" && git push`  
- [ ] LinkedIn Post #2 with your architecture photo  

---

## Part D — Keep repo demo-ready (habit)

Every week when you finish a module:

```powershell
git add .
git commit -m "Week X: short description"
git push
```

Update README if you add new endpoints.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `port 8001 in use` | Use `--port 8002` or stop other uvicorn |
| `python not found` | Install Python 3.11+ and tick "Add to PATH" |
| Push rejected | `git pull origin main --rebase` then push again |
| `.venv` in git by mistake | Should be ignored — run `git rm -r --cached backend/.venv` if needed |

---

## What to put on LinkedIn after repo is live

```
I'm building NexusOps — a Kubernetes management console for teams who don't want kubectl.

Week 1: live API demo is on GitHub.
Clone → run → open /docs

🔗 github.com/YOUR_USERNAME/nexusops-platform

Building in public. DM for early pilot conversations.

#Kubernetes #DevOps #PlatformEngineering #Ireland
```

Replace `YOUR_USERNAME` with your GitHub handle.
