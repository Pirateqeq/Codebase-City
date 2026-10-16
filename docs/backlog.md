# Product Backlog

Everything that could go into Codebase City, ordered from most to least important. The developer, as Product Owner, owns this file: agents read it but never edit it.

- **Ready:** detailed enough to pull into a sprint
- **Rough:** an idea that gets detailed when it moves up
- **Done:** finished stories, kept for the record

## Epics

| ID | Epic |
|---|---|
| E1 | Foundation: repo, environments |
| E2 | Repository analysis: fetch, scan, read history |
| E3 | Storage: SQLite database |
| E4 | Layout: turn the folder tree into building positions |
| E5 | API: endpoints from the contracts |
| E6 | City rendering: the Three.js scene |
| E7 | Interaction and pages: camera, hover, Home page |
| E8 | Polish and performance |
| E9 | Hosted demo |
| E10 | Hosted analysis (stretch) |

## Ready

2. **[E2]** As a user, I can point the analyzer at a repository on my computer and get every tracked file with its line count. (Tasks 1-6 Done, 7-12 Remaining)
   - A test helper builds a fixture repo in a temporary folder on each run, with known files, line counts, and 2 commits, including one ignored file, one untracked file, and one staged but uncommitted file (with a test proving its files, line counts, and commits)
   - Output exactly matches the fixture repo's known files and line counts
   - Only files in the latest commit are included; ignored, untracked, and staged but uncommitted files are left out
   - Lines are counted the way an editor shows them: a last line without a newline still counts, an empty file is 0, and `\r\n` counts the same as `\n`
   - Takes the repo path and the output file path as inputs, and saves a JSON file that uses the contract's field names (`buildings`, `path`, `metrics.lines`)
   - `buildings` is sorted by `path`, case-sensitive, by character code, using paths as Git stores them
   - A missing path or a folder that isn't a Git repo gives a clear error and writes no file; a repo with no commits gives an empty `buildings` list
   - *A local path for now; GitHub URLs come with the repo fetcher story.*

3. **[E6]** As a user, I can open a page and see each file as a 3D box.
   - One box per file in the JSON
   - Box size reflects line count *(temporary mapping until city mapping is designed)*
   - The page loads with no errors in the browser console

## Rough

4. **[E7]** As a user, I can orbit and zoom around the city.
5. **[E2]** As a user, I can see how often each file has changed (commit count).
6. **[E7]** As a user, I can hover over a building and see its details.
7. **[E3]** Analysis results are saved, so a city reopens without re-analyzing.
8. **[E5]** The API serves analyses and city data, following the contracts in the README.
9. **[E2]** As a user, I can paste a GitHub URL and the repo is cloned locally.
10. **[E7]** As a user, I can start an analysis from the Home page and see its progress.
11. **[E4]** As a user, I can see files grouped into districts by folder.
12. **[E2]** Binary files are handled correctly by the analyzer (skipped or counted, to be decided).
13. **[E2]** Committed files with uncommitted edits are analyzed as they are in the latest commit, with a test.

## Later

- Analyze a local folder from the Home page
- Re-analyze a repository after it changes
- Support folders that aren't Git repositories
- Hosted demo with sample repositories
- Hosted analysis (stretch goal)
- Replace the Vite Starter files

## Done

1. **[E1] Enabler:** Set up the project so code can be written and tested. *(Sprint 1)*