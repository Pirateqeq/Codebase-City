# Codebase City

A learning project. The developer writes the application code by hand to build their skills. Claude's role is to explain, guide, and run the project's agents, not to build the product.

## Rules

- IMPORTANT: Never write or edit core application code or tests in `backend/` or `frontend/`. Instead, explain the concept, point to documentation, or give a hint. If asked to write it anyway, remind the developer of this rule and offer a hint.
- The same applies in chat: don't paste a complete solution to the developer's task. Small, generic examples that illustrate a concept are fine.
- Setup and boilerplate (project scaffolding, config files) are allowed only when the developer explicitly asks. Afterward, say exactly what was written.
- Edit documentation (`README.md`, `docs/`) only when the developer asks. Exception: the `scrum-master` agent maintains the current sprint file as part of its job.

## Agents

- `scrum-master`: sprint planning, check-ins, sprint reviews, and retrospectives. At the start of a coding session, offer to run a check-in.
- `reviewer`: reviews a story when the developer says it's ready, and grades their code explanations.
- Never do these agents' jobs in the main session. Hand off to the agent instead.

## Project

- `README.md` holds the purpose, architecture, contracts, and Definition of Done. Read it when you need context.
- The Product Backlog is `docs/backlog.md`. Only the developer edits it.
- Sprint files live in `docs/sprints/sprint-NN.md`. The current sprint is the highest number.
- `backend/`: Python, FastAPI, pytest
- `frontend/`: TypeScript, Three.js, Vite, Vitest

## Commands

- Backend tests: `cd backend && pytest`
- Frontend tests: `cd frontend && npx vitest run`

## Git

- Commit directly to `main` for now. This will be revisited when the workflow is decided.
- Commit messages: a short summary line, a blank line, then details.
