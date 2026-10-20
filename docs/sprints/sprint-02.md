# Sprint 02

**Dates:** 2026-10-19 to 2026-10-25
**Sprint goal:** The analyzer outputs every file in a local repository's latest commit with its line count.

## Sprint backlog
- [ ] Story: "As a user, I can point the analyzer at a repository on my computer and get every tracked file with its line count."
  - Epic: E2 Repository analysis: fetch, scan, read history
  - Acceptance criteria:
    - A test helper builds a fixture repo in a temporary folder on each run, with known files, line counts, and 2 commits, including one ignored file, one untracked file, and one staged but uncommitted file (with a test proving its files, line counts, and commits)
    - Output exactly matches the fixture repo's known files and line counts
    - Only files in the latest commit are included; ignored, untracked, and staged but uncommitted files are left out
    - Lines are counted the way an editor shows them: a last line without a newline still counts, an empty file is 0, and `\r\n` counts the same as `\n`
    - Takes the repo path and the output file path as inputs, and saves a JSON file that uses the contract's field names (`buildings`, `path`, `metrics.lines`)
    - `buildings` is sorted by `path`, case-sensitive, by character code, using paths as Git stores them
    - A missing path or a folder that isn't a Git repo gives a clear error and writes no file; a repo with no commits gives an empty `buildings` list
    - A local path for now; GitHub URLs come with the repo fetcher story
  - Tasks (1-6 were done in Sprint 01; the fixture table is in `docs/sprints/sprint-01.md`):
    - [x] 7. Count lines per file, and update `test_names_in_order` for dict-shaped buildings
    - [x] 8. Save the output as a JSON file, with a test
    - [ ] 9. Take the repo path and output path as inputs
    - [ ] 10. Handle bad input, with tests:
      - Missing path or not a Git repo: clear error, no file written
      - Repo with no commits: empty `buildings` list
    - [ ] 11. Update the README Testing section to describe the generated fixture
    - [ ] 12. Reviewer review and explain check, then push to main
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

## Sprint review

## Retrospective
