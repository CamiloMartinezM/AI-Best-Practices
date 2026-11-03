# Timed outline

About 45 minutes plus discussion: 49 slides including the title, nine section dividers and a discussion slide. Timings match the speaker notes; "No." is the number in the slide footer. Sections 2 and 3 are the groundwork any agent needs: version control, including worktrees for parallel agents, and an environment with automatic checks. A thread runs from section 1 to section 5: the better the repository is prepared, the shorter the request can be. Each idea is introduced before a slide relies on it, so the names of Pocock's skills first appear in section 6, which builds up skills one step at a time: the idea, the file, a collection, the books it draws on, then the workflow.

| No. | Time | Slide | Purpose |
|---|---|---|---|
| — | 0:00 | Title | Topic, presenter, group; an editor in which an agent removes a line and adds two, under the prompt that asked for it |
| 1 | 0:20 | One task, nine questions | The nine sections as nine practical questions |
| — | 1:00 | Divider 01: From asking questions to delegating work | |
| 2 | 1:10 | From a chat assistant to a coding agent | What changes when the model can act |
| 3 | 2:20 | Running example: split the data by specimen | Specimens, the overview area and the detail area inside it, micrographs on one pixel grid with one mask; why a random patch split leaks |
| 4 | 3:40 | A weak request | The request as a terminal prompt; the parts its vague phrases leave open, and the two it never mentions |
| 5 | 4:40 | A bounded task specification | Objective, context, constraints, acceptance criteria, verification as five cards; on the next click, "But …" and the catch, which the rest of the talk answers: too much to write for every task, and the agent may know a better way |
| — | 5:50 | Divider 02: Version control with git | |
| 6 | 6:00 | Version control: one folder, every version | Copies of files versus a history; commit, diff, branch, remote |
| 7 | 7:10 | Getting started takes five commands | The learning curve; what `.gitignore` keeps out of the history; screenshot of VS Code's Source Control panel |
| 8 | 8:10 | Why an agent needs version control | Screenshot of an agent's diff; checkpoint, then keep or discard the agent's edits, drawn as a short history; one branch or worktree per task |
| 9 | 9:20 | Worktrees: work in parallel, merge when done | One history, one folder and branch per worktree; `git worktree add`, `list`, `remove` |
| 10 | 10:30 | Parallel sessions in the Claude app and the terminal | The Worktree button under the prompt box (screenshot) and `claude --worktree` in a terminal; the same four stages in both: start, folder and branch, next task, done |
| — | 12:40 | Divider 03: Environments and code checks | |
| 11 | 12:50 | The classic setup: a conda environment | `environment.yml` and its commands; an agent runs each command in a new shell, so an activation does not carry over, unless the environment is active before the agent starts; uv, faster for Python-only projects, linked to its repository (backup slides A4, A5) |
| 12 | 13:50 | Ruff, mypy and Pylance | What each tool does and where it runs: VS Code, terminal, pre-commit, CI; type hints |
| 13 | 14:40 | What it looks like in VS Code | Screenshot with Ruff, Pylance and mypy findings |
| 14 | 15:30 | Set them up once | `pyproject.toml`, VS Code settings, the commands with conda |
| — | 16:30 | Divider 04: Preparing the repository | |
| 15 | 16:40 | `AGENTS.md` for the example | The file's four sections and what each one is for: the conda environment of slide 11, the checks of section 3 marked to run after every edit, two lines that point to the glossary and the ADRs |
| 16 | 17:50 | Which instruction files load? | Codex instruction chain for a session started in `src/sem_seg/data/` |
| 17 | 19:10 | `GLOSSARY.md` and `CODING_STANDARDS.md` | Vocabulary, with the request's word "sample" marked as one to avoid, and the rules a review checks; when each file is read |
| — | 20:20 | Divider 05: Architecture decision records | |
| 18 | 20:30 | What an ADR is, and when to write one | Nygard's format in one line; three criteria, from Pocock's skills, as overlapping circles; research decisions that meet all three, and what needs no ADR |
| 19 | 21:30 | ADR-0003: specimen-level splits | The example record; superseding without deleting |
| 20 | 22:30 | Six files, six jobs | The six files of sections 1, 4 and 5 on an agent session: `AGENTS.md` every session, glossary and ADRs when pointed to, the task specification with the task, coding standards in review, README for people |
| 21 | 23:30 | The same request, in a prepared repository | A one-sentence request; the five cards of slides 4 and 5, filled by files; what no file says stays open |
| — | 24:50 | Divider 06: Skills and an end-to-end workflow | |
| 22 | 25:00 | A skill: a lab protocol for the agent | A sample-preparation protocol beside an abridged `tdd/SKILL.md`, row for row: the name, when to use it, the steps |
| 23 | 26:00 | Skills: procedures loaded when needed | Pocock's `tdd/SKILL.md`, its parts marked by when they load: name and description from the start, the body when the skill runs, the files beside it when the steps need them; the skill folders of Claude Code and Codex |
| 24 | 27:10 | Pocock's skills: an open collection | The repository's address as a link over its screenshot; the skills you type and the skills they call; the install command |
| 25 | 28:00 | Classic practice, adapted for agents | Six books from 1999 to 2018, the idea the skills take from each and the skills that carry it, user stories for the spec among them; the README's "based on decades of engineering experience" |
| 26 | 29:10 | Pocock's flow: who does what | Person, agent and output across the five stages: spec-driven, then test-first |
| 27 | 30:20 | A /grill-with-docs session | Example session on the short request: numbered markers for a looked-up fact, a recommended answer and the ADR decision; an arrow to the glossary entry it adds |
| 28 | 31:40 | The specimen split, stage by stage | What each stage produces for the specimen split, under the columns of slide 26 |
| 29 | 32:50 | When is the full flow worth it? | Size and meaning of a change decide the route |
| — | 33:30 | Divider 07: Tests first | |
| 30 | 33:40 | Test-driven development: red, green, refactor | The loop, each step with what it gives us |
| 31 | 34:40 | Why tests first help an agent | Tests as the agent's pass-or-fail signal: what they give it, how they get gamed, what catches the gaming |
| 32 | 35:40 | How /implement uses /tdd | The five steps of a run; rules of the /tdd loop |
| 33 | 36:50 | Red and green on the specimen split | Four red-green cycles for ticket T1 |
| — | 38:00 | Divider 08: Safeguards and scientific verification | |
| 34 | 38:10 | Written rules versus enforced controls | Four rules as `AGENTS.md` states them, each backed by the control that holds anyway |
| 35 | 39:30 | Verifying the running example | The fold test; the checks before merging as four commands (scope of the diff, tests, fold check, raw-data checksums); the fold file that records seed, commit and manifest hash |
| 36 | 40:30 | Runs, passes the tests, is valid | Three claims as a ladder, each with who checks it; the HCCI specimen folds, where every held-out specimen is a new state with classes training never shows |
| — | 41:40 | Divider 09: A realistic starting point | |
| 37 | 41:50 | Other skill packages, one shared core | Pocock's skills, superpowers, andrej-karpathy-skills and GSD Core: who made each, what it is, its steps and its rule for tests; in all four the check is set before the code |
| 38 | 42:50 | Checklist for your repository | Groundwork, context and control |
| — | 43:40 | Questions and discussion | Projects without git, a first repository to try, decisions worth an ADR, verification command |

## Appendix

A1 `AGENTS.md` template; A2 glossary, coding-standards and ADR templates; A3 bounded task specification template; A4 the upgrade: uv, and A5 conda or uv?, both kept for questions after slide 11, with notes that start "If asked"; A6 how Codex finds instruction files; A7 Codex files, limits and controls; A8 Pocock's workflow in the July 2026 video and in v1.3.1; A9 to A12 references, A12 for the books behind Pocock's skills and the other skill packages.
