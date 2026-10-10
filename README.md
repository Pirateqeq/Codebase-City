# Codebase City

Codebase City turns a software repository into an interactive 3D city, so you can explore how a project is built instead of reading through it file by file.

**Who it's for:** Students and amateur developers who want to see what their projects would look like if they were cities.

**Status:** Planning and setup.

---

## Table of Contents

1. [Purpose](#purpose)
2. [Learning Goals](#learning-goals)
3. [What It Does](#what-it-does)
4. [Quality Attributes](#quality-attributes)
5. [Tech Stack](#tech-stack)
6. [Getting Started](#getting-started)
7. [Architecture](#architecture)
8. [Testing](#testing)
9. [Development Methodology](#development-methodology)
10. [Team](#team)

---

## Purpose

Build a polished, finished tool that turns codebases into explorable 3D cities, and develop real software engineering skills along the way.

---

## Learning Goals

- Data structures and algorithms
- Database and schema design
- API design
- Systems thinking
- 3D rendering basics
- Testing
- Agile development with Scrum

---

## What It Does

### City mapping

*To be designed.*

### Core features

- Paste a GitHub repository URL and analyze it on your own computer
- Explore the city in 3D: orbit, zoom, and hover for details

### Later

- Analyze a local folder
- Re-analyze a repository after it changes
- Support folders that aren't Git repositories
- Hosted demo with sample repositories
- Analyze repositories online without installing anything (stretch goal)

---

## Quality Attributes

In priority order:

**1. Correctness:** the city matches the codebase.

> **Why:** Wrong numbers would mislead users, which is worse than no city at all.

**2. Performance:** the city stays fast as projects grow.

> **Why:** Projects vary a lot in size, and a slow city ruins the experience.

**3. Visual polish:** it looks and feels finished.

> **Why:** The visuals are the reason to use this instead of a file tree.

---

## Tech Stack

| Layer | Choice | Why |
|---|---|---|
| 3D front end | Three.js + TypeScript | Teaches 3D fundamentals directly, runs in any browser, and types catch errors early |
| Build tool | Vite | The standard pairing for TypeScript and Three.js |
| Backend | Python + FastAPI | Familiar, great at parsing data, and generates API docs automatically |
| Database | SQLite locally, PostgreSQL hosted | SQLite needs no server; PostgreSQL handles many users |
| Testing | pytest and Vitest | The standard tools for Python and TypeScript |
| Version control | Git + GitHub | Industry standard, and my portfolio is already there |
| AI agents | Claude Code subagents | Agents live in the repo as files, and each one is limited to the tools it needs |
| Git analysis | *To be decided* | |
| Continuous integration | *To be decided* | |

---

## Getting Started

*These instructions are written for Windows (Command Prompt).*

### Requirements

- Git
- Python 3.14 or newer *(developed on 3.14.6)*
- Node.js 24 or newer, with npm *(developed on 24.14.1)*

### Install

```bash
git clone https://github.com/Pirateqeq/Codebase-City.git
cd Codebase-City
```

**Backend**

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate.bat # Windows
pip install -r requirements.txt
```

**Frontend**

```bash
cd ../frontend
npm install
```

### Run the tests

```bash
cd backend             # with the virtual environment active
pytest
cd ../frontend
npx vitest run
```

### Run the front end

```bash
cd frontend
npm run dev
```

---

## Architecture

### Deployment model: Hybrid

1. **Local-first:** runs on your computer and opens in the browser.
2. **Hosted demo:** a public site with sample repositories.
3. **Hosted analysis (stretch):** analyze any public repository online.

> **Why:** Running locally keeps code private and avoids hosting costs and security risks. The demo still lets anyone try it instantly.

### How it works

```
              Launcher: starts the local server and opens the browser
                                   │
PHASE 1 — ANALYZE (once per repo)  ▼
  Home page ──▶ API ──▶ Repo fetcher ──▶ Analyzer ─────────────────────▶ Database
  paste URL             git clone        Scanner → Git reader → Layout     (SQLite)
                                                                              │
PHASE 2 — VIEW (every visit)                                                  │
  City page ◀── city data (JSON) ── API ◀─────────────────────────────────────┘
```

### Components

| Component | Job |
|---|---|
| **Launcher** | Starts the local server and opens the browser |
| **Home page** | Takes a GitHub URL and shows progress |
| **API** | Connects the browser to the backend |
| **Repo fetcher** | Clones the repository into a local cache |
| **Scanner** | Lists tracked files and counts their lines |
| **Git history reader** | Finds each file's commit count and last change |
| **Layout engine** | Works out where each building goes and how big it is |
| **Database** | Stores each analysis and its status |
| **City page** | Draws the city and handles interaction |

### Contracts

**Start an analysis**

```
POST /api/analyses        { "source": { "type": "github", "url": "https://github.com/user/repo" } }
                        → { "analysis_id": "a1b2", "status": "queued" }

GET  /api/analyses/a1b2 → { "status": "queued | cloning | analyzing | done | failed" }
```

**Get city data**

```json
GET /api/analyses/a1b2/city
{
  "schema_version": 1,
  "repo": { "name": "repo", "source": "https://github.com/user/repo" },
  "buildings": [
    {
      "path": "src/cli.py",
      "metrics":  { "lines": 120, "commits": 14, "last_changed": "2026-10-05" },
      "geometry": { "x": 0, "z": 0, "width": 4, "depth": 4, "height": 14 }
    }
  ]
}
```

### Design decisions

| Decision | Choice | Why |
|---|---|---|
| Entry point | Browser, started with one command | A web page can't read files on its own |
| Input | GitHub URL now, local folders later | Matches how users think about their projects |
| Repositories | Git only, for now | Git provides the history and skips ignored files |
| Layout | Calculated on the backend | Keeps the front end simple and the algorithm easy to test |
| Long analyses | Job ID + status checks | Shows progress and avoids timeouts |
| Repo structure | One repo: `backend/` and `frontend/` | Everything lives in one place |
| Serving the front end | Vite while coding, FastAPI for users | Fast reloads for me, one server for users |
| Background jobs | FastAPI's built-in background tasks | A single local user doesn't need more |
| Clone depth | Full clones | Shallow clones would get commit counts wrong |
| Clone storage | Cached and reused | Makes re-analysis fast |
| Security | Local connections and github.com URLs only | Other devices on the network can't reach the server |

---

## Testing

| Test repositories | What they are | What they check |
|---|---|---|
| **Fixture repositories** | Small repos built for testing, with known answers | Correctness |
| **Real-world repositories** | Existing projects of different sizes | Performance and visual polish |

> **Why:** You can only test correctness when you already know the right answer. Real projects show how it holds up at scale.

*Specific repositories to be selected.*

---

## Development Methodology

This project uses **Scrum**: work happens in short, fixed-length **sprints**, and AI agents act as Scrum Master and Reviewer / Tester (see [Team](#team)).

> **Why:** Every sprint has to end with working software, which keeps the project moving instead of stuck in planning.

### How work is organized

```
Product Goal → Epics → User Stories → Tasks
```

| Level | What it is | Example |
|---|---|---|
| **Product Goal** | The long-term objective | The purpose above |
| **Epic** | A big chunk of work, too large for one sprint | "Repository analysis" |
| **User Story** | A small, user-facing piece that fits in one sprint | "As a user, I can paste a repo URL and see its files listed." |
| **Task** | One step toward finishing a story | "Clone the repository" |

Epics and user stories aren't part of the official Scrum Guide; they're common add-ons.

### Sprints

- Each sprint lasts one week.
- Each sprint has one goal, set at the start.
- Each sprint ends with something that works.

### Definition of Done

**Version 1.** Revisited at every retrospective.

Every user story is checked against this list. It's Done only when every item is true; otherwise it goes back to the backlog.

> **Why:** Stories are what users actually get. Checking each one catches problems early.

| Area | Requirement | Why |
|---|---|---|
| **Works** | Runs without errors on the fixture repositories *(to be selected)* | Proves it works on known data |
| **Correctness** | New logic has tests, and they pass | Proves it's correct instead of assuming it |
| **Correctness** | All existing tests still pass *(automated once CI is set up)* | New work can't break old work |
| **Performance** | Stays smooth on the large test repository *(threshold to be set)* | A slow city ruins the experience |
| **Visual polish** | *To be defined* | Needs a clear yes-or-no check first |
| **Reviewed** | The reviewer agent has checked it; issues are fixed or logged | A second pair of eyes |
| **Understood** | The reviewer's explain check is graded Correct | Code I can't explain is code I didn't learn from |
| **Integrated** | Committed and pushed to main *(branch workflow to be decided)* | Work only on my laptop doesn't count |
| **Documented** | README updated if behavior changed | Keeps the docs accurate |

### Workflow

- **Product Backlog:** `docs/backlog.md`
- **Sprint files:** `docs/sprints/sprint-NN.md`
- *Branch workflow to be decided.*

---

## Team

| Role | Filled by |
|---|---|
| **Product Owner** | Me |
| **Developer** | Me |
| **Scrum Master** | AI agent |
| **Reviewer / Tester** | AI agent |

> **Why:** The agents add structure and a review step I'd otherwise skip. I write the code because that's how I learn, and I stay Product Owner because AI tends to agree with whoever it's talking to.

### Scrum Master agent (`scrum-master`)

- Runs sprint planning and keeps each sprint goal focused
- Checks in during the sprint and flags blockers
- Flags scope creep
- Runs the sprint review and retrospective

### Reviewer / Tester agent (`reviewer`)

- Reviews finished work before it counts as Done
- Suggests test cases and edge cases
- Explains errors and failing tests

The agents are defined in `.claude/agents/scrum-master.md` and `.claude/agents/reviewer.md`. Project-wide rules for Claude live in `CLAUDE.md`.