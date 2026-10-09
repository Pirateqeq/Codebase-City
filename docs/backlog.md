# Product Backlog

Everything that could go into Codebase City, ordered from most to least important. The developer, as Product Owner, owns this file: agents read it but never edit it.

- **Ready:** detailed enough to pull into a sprint
- **Rough:** an idea that gets detailed when it moves up

## Epics

| ID | Epic |
|---|---|
| E1 | Foundation: repo, environments, test setup |
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

1. **[E1] Enabler:** Set up the project so code can be written and tested.
   - The repo contains the README, `CLAUDE.md`, the agents, and `.gitignore`
   - The backend virtual environment is set up and `pytest` runs
   - The frontend Vite project runs in the browser
   - A test helper can create a temporary Git repo with known files and commits

2. **[E2]** As a user, I can point the analyzer at a repository on my computer and get every tracked file with its line count.
   - Output exactly matches the fixture repo's known files and line counts
   - Ignored and untracked files are left out
   - Output is saved as a JSON file
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

## Later

- Analyze a local folder from the Home page
- Re-analyze a repository after it changes
- Support folders that aren't Git repositories
- Hosted demo with sample repositories
- Hosted analysis (stretch goal)
