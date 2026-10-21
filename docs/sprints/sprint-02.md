# Sprint 02

**Dates:** 2026-10-19 to 2026-10-25
**Sprint goal:** The analyzer outputs every file in a local repository's latest commit with its line count.

## Sprint backlog
- [x] Story: "As a user, I can point the analyzer at a repository on my computer and get every tracked file with its line count."
  - Epic: E2 Repository analysis: fetch, scan, read history
  - Acceptance criteria:
    - A test helper builds a fixture repo in a temporary folder on each run, with known files, line counts, and 2 commits, including one ignored file, one untracked file, and one staged but uncommitted file (with a test proving its files, line counts, and commits)
    - Output exactly matches the fixture repo's known files and line counts
    - Only files in the latest commit are included; ignored, untracked, and staged but uncommitted files are left out
    - Lines are counted the way an editor shows them: a last line without a newline still counts, an empty file is 0, and `\r\n` counts the same as `\n`
    - Takes the repo path and the output file path as inputs, and saves a JSON file that uses the contract's field names (`buildings`, `path`, `metrics.lines`)
    - `buildings` is sorted by `path`, case-sensitive, by character code, using paths as Git stores them
    - A missing path or a folder outside any Git repo gives a clear error and writes no file; a repo with no commits gives an empty `buildings` list
    - A local path for now; GitHub URLs come with the repo fetcher story
  - Tasks (1-6 were done in Sprint 01; the fixture table is in `docs/sprints/sprint-01.md`):
    - [x] 7. Count lines per file, and update `test_names_in_order` for dict-shaped buildings
    - [x] 8. Save the output as a JSON file, with a test (Test checks the file exists; output contents are verified through analyze_repo's returned dict.)
    - [x] 9. Take the repo path and output path as inputs
    - [x] 10. Handle bad input, with tests:
      - Missing path or not a Git repo: clear error, no file written
      - Repo with no commits: empty `buildings` list
    - [x] 11. Update the README Testing section to describe the generated fixture
    - [x] 12. Reviewer review and explain check, then push to main
  - Reminder: demo the working output to at least one real person once the JSON file exists.

## Daily log

### 2026-10-19
- **Done:** Nothing yet.
- **Next:** Task 7.
- **Blocker:** Finding a neat way to count lines for different file types from blob bytes. **Next step (not code):** List the line-ending cases from the criteria (no final newline, empty file, `\r\n`) as a short table of input and expected count, and check any approach against it.

### 2026-10-20
- **Done:** Tasks 7 and 8.
- **Next:** Tasks 9 and 10.
- **Blocker:** None.
- **Risk:** Task 10 (bad input) may take most of the available time. **Next step (not code):** List every bad-input case from the criteria (missing path, folder that isn't a Git repo, repo with no commits, no file written on error) as a short table of input and expected result, then order them by effort and start with the smallest.
- **Flag:** Task 8's test only checks that the output file exists, not its contents. The criteria require output that exactly matches the known files and line counts.

### 2026-10-21
- **Done:** Tasks 9 and 10.
- **Next:** Tasks 11 and 12.
- **Blocker:** None.
- **Decision:** Developer considers task 8's test done, because the tests check the output's buildings, paths, and line counts.
- **Flag:** No demo logged yet. Demo the working output to a real person before the sprint review.
- **Flag:** Start task 12 by about 10-23 so review fixes fit before the sprint ends on 10-25.

## Sprint review

**Closed:** 2026-10-21 (early; scheduled end 2026-10-25). **Hours used:** about 15.

**Done**
- Story: "As a user, I can point the analyzer at a repository on my computer and get every tracked file with its line count." Met the Definition of Done: reviewer verdict Ready, explain check graded Correct, 23 tests pass, pushed to main (3193ffd).

**Not done**
- None.

**Returned to backlog**
- None. Reminder: move Story 2 to Done in `docs/backlog.md`.

**Demo**
- No demo was given. Developer's reason: the analyzer alone has no outside audience, so they judged the output JSON themselves and it looks good.

**Sprint goal**
- Met: the analyzer outputs every file in a local repository's latest commit with its line count.

## Retrospective

**What worked:** Doing two tasks at once. Getting the hang of making and using tests.

**What didn't:** Nothing major; everything worked as expected. Newer material took more time, as expected.

**One change next sprint:** When planning a story, check whether it can be demoed at all. Some stories, like this analyzer-only one, are hard to show.

**Also noted:** Define the Performance row of the Definition of Done next sprint, since upcoming work may read and store larger repos. Next sprint will probably be E3 (context, not a commitment).

**Definition of Done proposal (developer edits the README):**
- Replace "threshold to be set" in the Performance row with a measurable check on a named test repository. It could cover: which repository counts as "large", what is measured (analysis time, and later store/load time), and the pass limit.
- Example: "Analyzing the large test repository finishes in under 30 seconds on my laptop."
