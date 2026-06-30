# Step-by-Step — You Do Everything (Demo + Pitch Ready)

Follow this guide **yourself**. Every command is run **by you**.  
That way you can honestly say: *"I set up the repo, wrote the code, and pushed it."*

**Using Ubuntu (WSL) + VS Code?** → Jump to **[Ubuntu / WSL + VS Code](#ubuntu--wsl--vs-code)** below.

**Using Windows PowerShell?** → Use the PowerShell sections in Part B onward.

---

## Ubuntu / WSL + VS Code

### 0 — One-time setup on Ubuntu (5 min)

Open **Ubuntu** terminal (WSL) and run:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git
python3 --version   # should be 3.10+
git --version
```

### 1 — Find your project in WSL

If the project is on Windows under `C:\Users\User\Projects\`:

```bash
cd /mnt/c/Users/User/Projects/nexusops-platform
ls
```

You should see: `README.md`, `docs`, `learn`, `backend`.

**Tip:** For faster Git/Python on WSL, copy the project into Linux home later:

```bash
cp -r /mnt/c/Users/User/Projects/nexusops-platform ~/nexusops-platform
cd ~/nexusops-platform
```

Either path works for Week 1.

### 2 — Open in VS Code

From the project folder in Ubuntu terminal:

```bash
code .
```

If `code` is not found:

1. Open VS Code on Windows  
2. Install extension: **WSL** (Microsoft)  
3. In Ubuntu terminal: `code .` again  

Or: VS Code → **File → Open Folder** → `\\wsl$\Ubuntu\home\YOUR_USER\nexusops-platform`

### 3 — GitHub repo (browser — same for everyone)

1. https://github.com → **New repository**  
2. Name: `nexusops-platform`  
3. **Public**, **no** README  
4. Copy URL: `https://github.com/YOUR_USERNAME/nexusops-platform.git`

### 4 — First commit and push (Ubuntu terminal)

```bash
cd /mnt/c/Users/User/Projects/nexusops-platform
# OR: cd ~/nexusops-platform

git config user.name "Your Name"
git config user.email "your.email@example.com"

git add .
git status
git commit -m "Initial commit: NexusOps platform docs, Week 1 learning track, and reference backend"

git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/nexusops-platform.git
git push -u origin main
```

If `remote origin already exists`:

```bash
git remote set-url origin https://github.com/YOUR_USERNAME/nexusops-platform.git
git push -u origin main
```

### 5 — Week 1 API (Ubuntu terminal)

```bash
cd learn/week-01
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```

Open in browser (Windows browser is fine):

- http://localhost:8001/health  
- http://localhost:8001/docs  

### 6 — Add `/about` in VS Code

1. In VS Code, open `learn/week-01/main.py`  
2. Add below `/health`:

```python
@app.get("/about")
def about():
    return {
        "name": "NexusOps",
        "tagline": "Kubernetes management console for teams who don't want kubectl",
        "version": "0.1.0-week1",
    }
```

3. Save (Ctrl+S) — server reloads  
4. Test: http://localhost:8001/about  

### 7 — Commit your work (new Ubuntu terminal tab)

```bash
cd /mnt/c/Users/User/Projects/nexusops-platform
git add learn/week-01/main.py
git commit -m "Week 1: add /about endpoint for product demo"
git push
```

### VS Code tips

| Task | How |
|------|-----|
| Terminal in VS Code | `` Ctrl+` `` or **Terminal → New Terminal** (pick **Ubuntu/WSL**) |
| Python venv in VS Code | `Ctrl+Shift+P` → **Python: Select Interpreter** → `./learn/week-01/.venv/bin/python` |
| Run server | Terminal: `source .venv/bin/activate` then `uvicorn main:app --reload --port 8001` |
| Stop server | `Ctrl+C` in terminal |

### Ubuntu troubleshooting

| Problem | Fix |
|---------|-----|
| `python3: command not found` | `sudo apt install python3 python3-venv python3-pip` |
| `code: command not found` | Install VS Code WSL extension; reopen Ubuntu |
| `git push` auth fails | Use GitHub PAT or `gh auth login` |
| Port 8001 in use | `uvicorn main:app --reload --port 8002` |
| Slow git on `/mnt/c/` | Copy project to `~/nexusops-platform` |

---

## Part A — Create GitHub repo (10 minutes)

### Step 1 — Log in to GitHub

1. Open https://github.com  
2. Sign in to your account  

### Step 2 — Create empty repository

1. Click **+** (top right) → **New repository**  
2. Fill in:
   - **Repository name:** `nexusops-platform` (or your brand name)  
   - **Description:** `Multi-cloud Kubernetes management console — enterprise-style admin UI for K8s`  
   - **Public** (so anyone can view demo)  
   - **Do NOT** tick "Add a README" (you already have files locally)  
3. Click **Create repository**  
4. **Keep the page open** — you need the URL, e.g.  
   `https://github.com/YOUR_USERNAME/nexusops-platform.git`

---

## Part B — Push your local project (15 minutes)

Open **PowerShell** and run **one block at a time**. Wait for each to finish.

### Step 3 — Go to project folder

```powershell
cd C:\Users\User\Projects\nexusops-platform
```

### Step 4 — Check files are there

```powershell
dir
```

You should see: `README.md`, `docs`, `learn`, `backend`, etc.

### Step 5 — Configure git (first time only on this PC)

```powershell
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

Use the **same email** as your GitHub account.

### Step 6 — First commit (you own this commit)

```powershell
git add .
git status
```

Confirm `.venv` and `*.db` are **not** listed (they are in `.gitignore`).

```powershell
git commit -m "Initial commit: NexusOps platform docs, Week 1 learning track, and reference backend"
```

### Step 7 — Connect to GitHub and push

Replace `YOUR_USERNAME` with your GitHub username:

```powershell
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/nexusops-platform.git
git push -u origin main
```

If asked to log in, use GitHub browser login or Personal Access Token.

### Step 8 — Verify

Refresh your GitHub repo page. You should see all files and README.

**Pitch line:** *"I published the project on GitHub so teams can clone and run the Week 1 demo."*

---

## Part C — Week 1 demo (you build — 1 to 2 hours)

Anyone cloning your repo starts here. **You do this first** so you've lived it.

### Step 9 — Week 1 folder

```powershell
cd C:\Users\User\Projects\nexusops-platform\learn\week-01
```

### Step 10 — Python environment

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### Step 11 — Run API

```powershell
uvicorn main:app --reload --port 8001
```

Leave this window open. Open browser:

- http://localhost:8001/health  
- http://localhost:8001/docs  

### Step 12 — YOU add `/about` (your first feature)

1. Open `learn/week-01/main.py` in Cursor  
2. Below the `/health` function, add:

```python
@app.get("/about")
def about():
    return {
        "name": "NexusOps",
        "tagline": "Kubernetes management console for teams who don't want kubectl",
        "version": "0.1.0-week1",
    }
```

3. Save — server reloads automatically  
4. Test: http://localhost:8001/about  

### Step 13 — Commit YOUR code

Open a **new** PowerShell (keep server running or stop with Ctrl+C):

```powershell
cd C:\Users\User\Projects\nexusops-platform
git add learn/week-01/main.py
git commit -m "Week 1: add /about endpoint for product demo"
git push
```

**Pitch line:** *"Week 1 I shipped the first API endpoints — health check and product about page."*

---

## Part D — Share demo with anyone (5 minutes)

Send them this:

### For viewers (clone + run)

**Ubuntu / WSL / Mac:**

```bash
git clone https://github.com/YOUR_USERNAME/nexusops-platform.git
cd nexusops-platform/learn/week-01
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```

**Windows PowerShell:**

```powershell
git clone https://github.com/YOUR_USERNAME/nexusops-platform.git
cd nexusops-platform\learn\week-01
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```

Then open: http://localhost:8001/docs  

### What they see

- **Product name:** NexusOps  
- **Live API docs** (Swagger)  
- **`/health`** — platform is running  
- **`/about`** — what you're building (after you add it)  

Add your repo URL to LinkedIn **Featured** section.

---

## Part E — How to pitch (30-second script)

Use this when talking to companies or on LinkedIn:

> I'm building **NexusOps** — a Kubernetes management console for teams who don't want to live on kubectl.  
> Same idea as enterprise admin consoles: one browser UI for all clusters — AWS, Azure, GCP, on-prem.  
> We add **roles**, **incident tracking with MTTD/MTTR**, and **multi-cloud billing**.  
> I've open-sourced the journey on GitHub — Week 1 API is live; we're building in public.  
> **[Your GitHub URL]** — clone it and open `/docs` for a quick demo.

---

## Part F — LinkedIn (after Step 13)

1. Open `docs/LINKEDIN-PLAYBOOK.md`  
2. Post **Week 1 Post #1**  
3. Add line: *"Repo link in comments"* → paste your GitHub URL  

---

## Part G — Weekly rhythm (2–3 hours/day)

| When | You do |
|------|--------|
| **Mon–Wed** | Read week README in `learn/week-XX/` + code one feature |
| **Thu** | Test + `git commit` + `git push` |
| **Fri** | LinkedIn post from playbook |

Each week = one new capability + one commit message you can explain in an interview.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `git push` asks for password | Use GitHub Personal Access Token, not account password |
| Port 8001 in use | Use `--port 8002` |
| `python` not found | Install Python 3.11+ from python.org, tick "Add to PATH" |
| `.venv` shows in `git status` | Run `git rm -r --cached .venv` then commit |

---

## Checklist — you are demo-ready when:

- [ ] GitHub repo is **public** and pushed  
- [ ] `/health` and `/about` work on your machine  
- [ ] You made **at least 2 commits** yourself (initial + Week 1)  
- [ ] LinkedIn post with repo link  
- [ ] You can screen-share `/docs` in 5 minutes  

---

## What comes next (after you finish Part C)

Message in chat: **"Week 1 done — open Week 2"**  

Week 2 you will (still **you** coding):

- Split API into folders  
- Add `/api/v1` prefix  
- Proper project structure  

We guide — **you type and commit**.
