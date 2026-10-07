# Codebase City

> Point it at a codebase. Walk through it as a 3D city.

<br>

Codebase City turns a software repository into an interactive 3D city, so you can explore the structure of a codebase visually instead of reading through it file by file.

**Who it's for:** Students and amateur developers who want to look at their own projects and get a better sense of how they are shaped.

> **Why:** I'm part of this group and understand its needs firsthand, and student-sized projects keep the first version's scope realistic.

**Status:** Planning — research and setup.

<br>

---

<br>

## Table of Contents

1. [Purpose](#purpose)
2. [Learning Goals](#learning-goals)
3. [What It Does](#what-it-does)
4. [Quality Attributes](#quality-attributes)
5. [Architecture](#architecture)
6. [Tech Stack](#tech-stack)
7. [Testing](#testing)
8. [Development Methodology](#development-methodology)
9. [Team](#team)

<br>

---

<br>

## Purpose

Build a polished, finished tool that turns codebases into explorable 3D cities, while developing transferable software engineering skills through a real development process.

<br>

---

<br>

## Learning Goals

- Data structures and algorithms
- Database and schema design
- API design
- Systems thinking
- 3D rendering basics
- Testing
- Agile development with Scrum

<br>

---

<br>

## What It Does

### City mapping

*To be designed.*

<br>

### Core features

- Analyze a repository on your own computer
- Explore the city in 3D: orbit, zoom, and hover for details

<br>

### Later

- Hosted demo with pre-analyzed sample repositories
- Paste a public GitHub URL to analyze it online (stretch goal)

<br>

---

<br>

## Quality Attributes

In priority order:

<br>

**1. Correctness** — the city accurately reflects the codebase.

> **Why:** Wrong metrics would mislead users, which is worse than having no city at all.

**2. Performance** — stays fast and interactive as projects grow.

> **Why:** Project sizes vary widely, and a slow city breaks the experience.

**3. Visual polish** — looks and feels finished.

> **Why:** The visual experience is the reason to use this tool instead of reading a file tree.

<br>

---

<br>

## Architecture

### Deployment model: Hybrid

1. **Local-first:** runs on the user's own computer; the city opens in the browser.
2. **Hosted demo:** a public site showing pre-analyzed sample repositories.
3. **Hosted analysis (stretch):** analyze any public GitHub repository online.

> **Why:** Running locally keeps users' code private and avoids server costs, security risks, and GitHub rate limits. A hosted demo still lets anyone try the tool instantly.

<br>

### System design

*To be designed.*

<br>

---

<br>

## Tech Stack

| Layer | Choice | Why |
|---|---|---|
| 3D front end | Three.js + TypeScript | Teaches 3D fundamentals directly without an extra framework layer, runs in the browser with no install, and TypeScript's types catch errors early. |
| Backend | Python + FastAPI | Python is familiar and strong at text parsing and data processing; FastAPI validates data with type hints and generates API docs automatically. |
| Database | SQLite (local) → PostgreSQL (hosted) | SQLite is a single file with no server, which fits a local tool; PostgreSQL handles many users at once and is the industry standard for hosted apps. |
| Testing | pytest (backend), Vitest (front end) | The standard testing tools for Python and TypeScript. |
| Version control | Git + GitHub | The industry standard, and my portfolio already lives on GitHub. |
| Git analysis | *To be decided* | |
| Continuous integration | *To be decided* | |

<br>

---

<br>

## Testing

The tool is tested against two kinds of test repositories:

| Kind | What it is | Checks |
|---|---|---|
| **Fixture repositories** | Small repositories built for testing, with known answers (exact files, line counts, and commit history) | Correctness |
| **Real-world repositories** | Existing projects of small, medium, and large size | Performance and visual polish |

> **Why:** Correctness can only be tested when the right answer is known in advance, which fixture repositories provide. Real-world repositories show how the tool behaves at realistic scale.

*Specific test repositories to be selected.*

<br>

---

<br>

## Development Methodology

This project is developed using the **Scrum framework**, an Agile approach where work is delivered in short, fixed-length iterations called **sprints**. AI agents fill the **Scrum Master** and **Reviewer / Tester** roles (see [Team](#team)).

> **Why:** Scrum requires each sprint to end with working software, which keeps the project shipping instead of stuck in planning. Research also suggests Scrum can be adapted for a solo developer.

<br>

### How work is organized

Work is broken down from large to small:

```
Product Goal → Epics → User Stories → Tasks
```

| Level | What it is | Example |
|---|---|---|
| **Product Goal** | The long-term objective for the whole project | The purpose statement above |
| **Epic** | A large body of work, too big for one sprint, grouped by theme | "Repository analysis" |
| **User Story** | A small, user-facing piece of an epic that fits within one sprint | "As a user, I can point the tool at a folder and see its files listed." |
| **Task** | A concrete step needed to complete a story | "Read the folder tree recursively" |

Epics organize work by **theme**; sprints organize work by **time**. A single sprint can include stories from several epics.

> **Note:** The Product Goal and sprints come from the Scrum Guide. Epics and user stories are not defined in the Scrum Guide; they are widely used practices that teams add on top of Scrum to organize their backlog.

<br>

### Sprints

- Each sprint is a fixed time-box (length *to be decided*).
- Each sprint has **one sprint goal**, chosen at the start.
- Each sprint ends with a **working increment**: something that runs, not just a plan.

<br>

### Definition of Done

**Version 1** — reviewed and tightened at each sprint retrospective.

The Definition of Done is checked for **each user story**. A story is Done only when **every** item below is true. If any item fails, the story is not shown at the sprint review and returns to the backlog.

> **Why:** User stories are the user-facing pieces that make up each increment. Tasks are too small to deliver value on their own, and checking only at the end of a sprint would catch problems too late.

| Area | Requirement | Why |
|---|---|---|
| **Works** | Runs without errors on the fixture repositories *(repositories to be selected)* | Proves the story works on data with known answers, not just on my machine by luck. |
| **Correctness** | New logic has automated tests, and they pass | Correctness is the top quality attribute; tests prove it instead of assuming it. |
| **Correctness** | All existing tests still pass *(automated once CI is decided)* | Each increment must work with everything built before it; nothing old can break. |
| **Performance** | Stays smooth on the large real-world test repository *(threshold to be defined)* | Project sizes vary widely, and a slow city breaks the experience. |
| **Visual polish** | *To be defined* | Polish is a core quality attribute but needs a yes-or-no check before it can be enforced. |
| **Reviewed** | The Reviewer / Tester agent has reviewed the work, and every issue is fixed or logged as a new backlog item *(review process to be researched)* | Adds a second check that a solo developer would otherwise skip. |
| **Understood** | I can explain every line of the new code *(verification method to be researched)* | Building skill is half the project's purpose; code I can't explain is code I didn't learn from. |
| **Integrated** | Committed, pushed to GitHub, and merged into the main branch *(branch workflow to be decided)* | Work that only exists on my computer isn't part of the increment. |
| **Documented** | README updated if the story changed how the tool behaves | Keeps the documentation accurate as the project grows. |

<br>

### Workflow

*To be researched.*

<br>

---

<br>

## Team

| Role | Filled by |
|---|---|
| **Product Owner** | Me |
| **Developer** | Me |
| **Scrum Master** | AI agent |
| **Reviewer / Tester** | AI agent |

> **Why:** Agents add process structure and a review step that a solo developer would otherwise skip. I keep the Developer role because writing the code myself is how this project builds skill, and the Product Owner role because AI assistants tend to agree with their users and can't represent real user needs independently.

<br>

### Scrum Master agent

**Responsibilities:**

- Facilitates sprint planning and checks that each sprint goal is a single, clear outcome
- Runs check-ins during the sprint and flags blockers
- Flags scope creep
- Facilitates the sprint review and retrospective

<br>

### Reviewer / Tester agent

**Responsibilities:**

- Reviews completed work before it is considered finished
- Suggests test cases and edge cases
- Explains errors and failing tests

<br>

*How the agents operate is to be researched.*