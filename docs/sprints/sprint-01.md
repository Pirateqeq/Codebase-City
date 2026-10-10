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
  - Acceptance criteria (matches `docs/backlog.md` as of 2026-10-10):
    - A test helper builds a fixture repo in a temporary folder on each run, with known files, line counts, and 2 commits, including one ignored file, one untracked file, and one staged but uncommitted file (with a test proving its files, line counts, and commits)
    - Output exactly matches the fixture repo's known files and line counts
    - Only files in the latest commit are included; ignored, untracked, and staged but uncommitted files are left out
    - Lines are counted the way an editor shows them: a last line without a newline still counts, an empty file is 0, and `\r\n` counts the same as `\n`
    - Takes the repo path and the output file path as inputs, and saves a JSON file that uses the contract's field names (`buildings`, `path`, `metrics.lines`)
    - A missing path or a folder that isn't a Git repo gives a clear error and writes no file; a repo with no commits gives an empty `buildings` list
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
  - Tasks (hour estimates are the Scrum Master's, not the developer's):
    - [ ] 1. Write the expected output by hand from the fixture table (~0.5h)
    - [ ] 2. Decide the Git analysis approach and record it in the README (~1h)
    - [ ] 3. Build the test helper that creates the temporary Git repo (~2h)
    - [ ] 4. Test the helper's files, line counts, and commits (~1h)
    - [ ] 5. Write a failing test: the analyzer's output matches the expected output (~0.75h)
    - [ ] 6. Implement the scanner for files in the latest commit (~2h)
    - [ ] 7. Count lines per file (~1.5h)
    - [ ] 8. Save the output as a JSON file, with a test (~1h)
    - [ ] 9. Take the repo path and output path as inputs (~1h)
    - [ ] 10. Handle bad input, with tests: path missing or not a Git repo -> clear error, no file written; repo with no commits -> empty `buildings` list (~1.5h)
    - [ ] 11. Update the README Testing section to describe the generated fixture (~0.5h)
    - [ ] 12. Reviewer review and explain check, then push to main (~1.5h)
    - Estimated total: ~14.25h of ~18h remaining (about 3.75h buffer)

## Daily log

### 2026-10-09
- **Done:** Nothing at check-in (day 1 of 7; start shifted from 10-08). All 8 Story 1 tasks were completed afterward (see 10-10).
- **Next:** Try to finish all 8 tasks today.
- **Blockers:** None. Some tools are unfamiliar, so research time is expected.
- **Watch:** All 8 in one session is optimistic. Commit after each task.

### 2026-10-10
- **Done:** Story 1 is Done: pushed to origin/main (1127b33, working tree clean), pytest and vitest each pass, explain check graded Correct (after rework on Q2 and Q3). Should-fix items (UTF-16 `requirements.txt`, empty root `main.py`) were fixed.
- **Blockers:** None.
- **Scope change:** Story 1 took about 3 of 21 hours, so the developer pulled Story 2 in. **Sprint goal changed mid-sprint** from "The project has its dependencies installed and tests set up for development." to the current goal, because the old goal was already met and Story 2 did not fit it.
- **Backlog sync:** Story 2 criteria above match the updated `docs/backlog.md`. The developer also added backlog items for replacing the Vite starter files and moving backend tests into their own folder.

## Sprint review

**Status:** Interim (2026-10-10). The sprint continues with Story 2; a final review will be added at sprint end.

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
- The developer did not see the two should-fix items as urgent but found them worthwhile.

**One thing that changes next sprint**
- Better judgement of timelines. To make this concrete: write an hours estimate next to each task before starting, and record actuals in the daily log.

**Definition of Done**
- No change proposed. Open from the reviewer: the "Works" (fixture repositories), "Performance", and "Visual polish" rows have no clear yes/no checks yet. The developer edits the README.
