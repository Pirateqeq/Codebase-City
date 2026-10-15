# Sprint 01

**Dates:** 2026-10-09 to 2026-10-15
**Sprint goal:** The analyzer outputs every file in a local repository's latest commit with its line count.

## Sprint backlog
- [x] Story: "Enabler: Set up the project so code can be written and tested."
  - Epic: E1 Foundation: repo, environments, test setup
  - Acceptance criteria:
    - The repo contains the README, `CLAUDE.md`, the agents, and `.gitignore`
    - The backend virtual environment is set up and `pytest` runs
    - The frontend Vite project runs in the browser
  - Tasks:
    - [x] Check that README, `CLAUDE.md`, both agent files, and `.gitignore` are in the repo
    - [x] Create the backend virtual environment, install FastAPI and pytest, and record them in `requirements.txt`
    - [x] Add one trivial passing test and confirm `cd backend && pytest` runs
    - [x] Scaffold the frontend with Vite (TypeScript) and install Three.js and Vitest
    - [x] Confirm the Vite dev server loads in the browser with no console errors
    - [x] Add one trivial passing test and confirm `cd frontend && npx vitest run` runs
    - [x] Add a "Getting started" section to the README: how to install dependencies and run tests
    - [x] Commit after each task; at the end of the story, get the reviewer agent's review and explain check, then push to main
- [ ] Story: "As a user, I can point the analyzer at a repository on my computer and get every tracked file with its line count."
  - Epic: E2 Repository analysis: fetch, scan, read history
  - Acceptance criteria:
    - A test helper builds the fixture repo below in a temporary folder on each run, with a test proving its files, line counts, and commits
    - Output exactly matches the fixture repo's known files and line counts
    - Only files in the latest commit are included; the table shows what is left out
    - Lines are counted the way an editor shows them: a last line without a newline still counts, an empty file is 0, and `\r\n` counts the same as `\n`
    - Takes the repo path and the output file path as inputs, and saves a JSON file that uses the contract's field names (`buildings`, `path`, `metrics.lines`)
    - `buildings` is sorted by `path`, case-sensitive, by character code, using paths as Git stores them
    - A missing path or a folder that isn't a Git repo gives a clear error and writes no file
    - A repo with no commits gives an empty `buildings` list
    - A local path for now; GitHub URLs come with the repo fetcher story
  - Out of scope (backlog items 12 and 13): binary files; committed files with uncommitted edits
  - Fixture (2 commits; the helper sets Git name/email inside the temp repo and turns off `core.autocrlf`):

    | File | Content | Expected |
    |---|---|---|
    | `README.md` | 3 lines, ends with a newline | included, 3 |
    | `src/main.py` | 5 lines | included, 5 |
    | `src/empty.py` | empty | included, 0 |
    | `notes.txt` | 2 lines, no final newline | included, 2 |
    | `windows.txt` | 2 lines with `\r\n` endings | included, 2 |
    | `.gitignore` | 1 line: `*.log` | included, 1 |
    | `debug.log` | anything | excluded (ignored) |
    | `scratch.txt` | anything | excluded (untracked) |
    | `staged.py` | added but not committed | excluded (not in latest commit) |
  - Tasks:
    - [x] 1. Write the expected output by hand from the fixture table
    - [x] 2. Decide the Git analysis approach and record it in the README
    - [x] 3. Build the test helper that creates the temporary Git repo
    - [x] 4. Test the helper's files, line counts, and commits
    - [x] 5. Write a failing test: the analyzer's output matches the expected output
    - [ ] 6. Implement the scanner for files in the latest commit
    - [ ] 7. Count lines per file
    - [ ] 8. Save the output as a JSON file, with a test
    - [ ] 9. Take the repo path and output path as inputs
    - [ ] 10. Handle bad input, with tests:
      - Missing path or not a Git repo: clear error, no file written
      - Repo with no commits: empty `buildings` list
    - [ ] 11. Update the README Testing section to describe the generated fixture
    - [ ] 12. Reviewer review and explain check, then push to main

## Daily log

### 2026-10-09
- **Done:** Nothing yet.
- **Next:** Try to finish all 8 tasks today.
- **Blockers:** None. Some tools are unfamiliar, so research time is expected.
- **Watch:** All 8 in one session is optimistic.

### 2026-10-10
- **Done:** Story 1 is Done: pushed to main, pytest and vitest each pass, explain check graded Correct. The two should-fix items (UTF-16 `requirements.txt`, empty root `main.py`) were fixed.
- **Scope change:** Story 1 finished early, so the developer pulled Story 2 in. **Sprint goal changed mid-sprint** from "The project has its dependencies installed and tests set up for development." to the current goal, because the old goal was already met and Story 2 did not fit it.
- **Backlog:** Developer added items for replacing the Vite starter files and moving backend tests into their own folder.
- **Check-in (later session, first Story 2 session):**
  - **Done:** Nothing yet.
  - **Next:** Tasks 1-5.
  - **Blockers:** Inexperience with fixtures and tests will slow things down. **Blocker (risk):** designing the Git analysis approach (task 2). It gates tasks 3-9 and is the main risk to the sprint goal.
  - **Suggested step:** Time-box the task 2 research (e.g. 45-60 min). List 2-3 options for reading files from the latest commit, compare them on the fixture's rules (latest commit only, `\r\n`, no final newline), pick one, and note why. Tasks 1, 3, 4, and 5 don't depend on the choice.

### 2026-10-11
- **Done:** Tasks 1-3, each committed: expected output (09a6c9a), approach chosen and recorded in the README Tech Stack table: pygit2 (bfab005), pytest fixture building the temp repo in `backend/tests/conftest.py` (9d4d40d). The buildings sorting rule was added to the README contract (d36175e). Backend tests pass.
- **Unplanned work:** Moved `backend/test_example.py` into `backend/tests/`. This is the backlog "Move backend tests into their own folder" item, outside Story 2. Small and finished. Mark or remove that backlog item.
- **Next:** Task 4.
- **Blockers:** None. The task 2 risk is resolved.
- **Unplanned work:** README cleanup (removed unnecessary lines), not tied to a Story 2 task. Small; not yet committed.

### 2026-10-12
- **Done:** Task 4 committed (68c090d) and ticked (0eaaeb0). Tests cover the fixture's committed files, line counts, 2 commits, and the staged, untracked, and ignored states. Confirmed they fail when the helper breaks. Backend suite: 14 passed.

### 2026-10-13
- **Done:** No commits.

### 2026-10-14
- **Status:** 4 of 12 Story 2 tasks done; tasks 5-12 remain, 1 day left. **The sprint goal is at serious risk.**
- **Plan:** Push on today and tomorrow, get as much done as possible, and see where it ends. Story 2 is picked up in a later sprint if not Done at the review.
- **Blocker:** Task 5 (failing test) requires knowing what the analyzer is and what it outputs before it exists. **Next step (not code):** On paper, write the analyzer's interface from the acceptance criteria: its name, what it takes, and what it returns or writes. Then write the test against that.
- **Notes:** Nothing specific stopped work on 10-13. The README cleanup was already committed (48088c4, 10-11).
- **Done (end of day):** Task 5 committed (78fdb53) and ticked. The analyzer is split into `analyze_repo(repo_path) -> dict` and `write_repo_data(data, output_path)`. Added `pytest.toml` so tests can import the analyzer. The two new analyzer tests fail on their assertions as intended; the other 14 pass. Working tree clean. Story 2: 5 of 12 tasks done.

### 2026-10-15
- **Status:** Last day of the sprint. Tasks 6-12 remain.
- **Next:** Task 6, the scanner.
- **Blockers:** None.

## Sprint review

**Status:** Interim. The sprint continues with Story 2; a final review will be added at sprint end.

- **Done:** Story 1 (E1 Enabler).
- **Not done / returned to backlog:** None.
- **Velocity:** 1 story (8 tasks) in ~3 of ~21 hours. The capacity estimate was far too high for a setup story. Vite scaffolding and test setup were the slower tasks (inexperience with the tools). ~18 hours remain (~3 hours/day).
- **Demo:** Not demoed (setup only). Risk is low now, but no real person has seen the project yet. Demo when Story 2 produces visible output.

## Retrospective

**What worked**
- Task lists kept the story complete and accurate.
- The reviewer enforced the Definition of Done and checked the developer could explain the work.
- The sprint file logs are a useful paper trail.

**What didn't**
- Nothing significant. The explain check needed rework on Q2 and Q3 because of inexperience with Vitest.
- The two should-fix items were not urgent but worthwhile.

**One thing that changes next sprint**
- Better judgement of timelines.

**Definition of Done**
- No change proposed. Open from the reviewer: the "Works" (fixture repositories), "Performance", and "Visual polish" rows have no clear yes/no checks yet. The developer edits the README.
