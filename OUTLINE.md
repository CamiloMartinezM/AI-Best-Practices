# Timed outline

About 40 minutes plus discussion: 46 slides including the title, eight section dividers and a closing slide. Timings match the speaker notes; "No." is the number in the slide footer. Sections 2 and 5 are the groundwork any agent needs: an environment with automatic checks, and version control, including worktrees for parallel agents. A thread runs from section 1 to section 4: the better the repository is prepared, the shorter the request can be. Each idea is introduced before a slide relies on it, so test-driven development comes in section 6 and the names of Pocock's skills first appear in section 7, which builds up skills one step at a time: the idea, the file, a collection, the books it draws on, then the workflow.

| No. | Time | Slide | Purpose |
|---|---|---|---|
| — | 0:00 | Title | Topic, presenter, group; an editor in which an agent removes a line and adds two, under the prompt that asked for it |
| 1 | 0:20 | Outline | The eight sections in order: each title as on its divider, with the divider's question in short |
| — | 1:00 | Divider 01: From asking questions to delegating work | |
| 2 | 1:10 | From a chat assistant to a coding agent | What changes when the model can act |
| 3 | 2:20 | Running example: split the data by specimen | Specimens, the overview area and the detail area inside it, micrographs on one pixel grid with one mask; why a random patch split leaks |
| 4 | 3:40 | A weak request | The request as a terminal prompt; the parts its vague phrases leave open, and the two it never mentions |
| 5 | 4:40 | A bounded task specification | Objective, context, constraints, acceptance criteria, verification as five cards; on the next click, "But …" and the catch, which the rest of the talk answers: too much to write for every task, and the agent may know a better way |
| — | 5:50 | Divider 02: Environments and code checks | |
| 6 | 6:00 | The classic setup: a conda environment | `environment.yml` and its commands; an agent runs each command in a new shell, so an activation does not carry over, unless the environment is active before the agent starts; uv, faster for Python-only projects, linked to its repository (backup slides A3, A4) |
| 7 | 7:00 | Ruff, mypy and Pylance | One card per tool, each with a small example and where it runs: Ruff checks how the code is written (lint and format), mypy whether the types match, Pylance helps while you type in VS Code; together, Pylance while writing, Ruff and mypy as the checks you and the agent run |
| 8 | 8:00 | What it looks like in VS Code | Screenshot with Ruff, Pylance and mypy findings; its numbered markers also number the list beside it |
| 9 | 8:40 | Set them up once | `pyproject.toml`, the whole `.vscode/settings.json`, the commands with conda |
| — | 9:40 | Divider 03: Preparing the repository | |
| 10 | 9:50 | Setting up the repository | A standard layout adapted from Cookiecutter Data Science, linked over its folder tree, with one `AGENTS.md` at the root; as the project grows, an arrow splits `AGENTS.md` into `AGENTS.md`, `GLOSSARY.md` and `CODING_STANDARDS.md`, the rest of the tree in grey |
| 11 | 10:50 | `AGENTS.md` | The example file beside what to put in (commands, pointers, what needs approval, when the work is done, the reason behind a rule) and what to leave out (rules that clash or are out of date, vague wishes, "think carefully"), after Anthropic's and OpenAI's prompting guides |
| 12 | 12:10 | `GLOSSARY.md` and `CODING_STANDARDS.md` | What each file holds, as tags over an example: term and meaning, words to avoid (the request's "sample" among them), code names; seeds, input checks, tests, paths |
| — | 13:30 | Divider 04: Architecture Decision Records (ADRs) | |
| 13 | 13:40 | What an ADR is, and when to write one | Nygard's format in one line; three criteria, from Pocock's skills, as overlapping circles; research decisions that meet all three, and what needs no ADR |
| 14 | 14:40 | ADR-0003: specimen-level splits | The example record; superseding without deleting |
| 15 | 15:40 | When the agent reads each file | The files of sections 3 and 4, the README and the task specification on an agent session: `AGENTS.md` every session, glossary and ADRs when pointed to, the task specification with the task, coding standards in review, README for people |
| 16 | 16:30 | Remember the bounded task specification? | Slide 5's five cards in grey under a stamp with its warning, "too much to write for every task"; what repeats is now in files |
| 17 | 17:00 | The same request, in a prepared repository | A one-sentence request; the five cards of slides 4 and 5, filled by files; what no file says stays open |
| — | 18:00 | Divider 05: Version control with git | |
| 18 | 18:10 | Version control: one folder, every version | Copies of files versus a history; commit, diff, branch, remote |
| 19 | 19:20 | Getting started takes five commands | The learning curve: five commands, `git init` to `git push`; what `.gitignore` keeps out of the history; screenshot of VS Code's Source Control panel, each control labelled with its command |
| 20 | 20:20 | Why an agent needs version control | Screenshot of an agent's diff; checkpoint, then keep or discard the agent's edits, drawn as a short history; one branch or worktree per task |
| 21 | 21:30 | Worktrees: work in parallel, merge when done | What a worktree is, in two lines; one history, one folder and branch per worktree, drawn as two branches merged into `main`; `git worktree add`, `list`, `remove` beside the drawing |
| 22 | 22:30 | How to use worktrees? | The Worktree button under the prompt box (screenshot) and `claude --worktree` in a terminal; the same four stages in both: start, folder and branch, next task, done |
| 23 | 24:00 | Tip: when a session splits into two tasks, fork it | One session's conversation forked in two with `/fork`, each fork asking for a worktree, so both keep the conversation and work in folders of their own; the Claude app's sidebar with a session and its forks, numbered markers explained beside it; `claude -c --fork-session` in a second terminal |
| — | 24:50 | Divider 06: Tests first | |
| 24 | 25:00 | Test-Driven Development (TDD) | The loop, each step with what it gives us |
| 25 | 26:00 | Why tests first help an agent | Tests as the agent's pass-or-fail signal: what they give it, how they get gamed, what catches the gaming |
| — | 27:00 | Divider 07: Skills and an end-to-end workflow | |
| 26 | 27:10 | A skill: a lab protocol for the agent | A sample-preparation protocol beside a shortened `tdd/SKILL.md`, row for row: the name, when to use it, the steps; a strip: one procedure per kind of task, worth writing when the task recurs |
| 27 | 28:10 | A skill: procedures loaded when needed | Pocock's `tdd/SKILL.md`, its parts marked by when they load: name and description from the start, the body when the skill runs, the files beside it when the steps need them; the skill folders of Claude Code and Codex |
| 28 | 29:20 | Matt Pocock's skills: an end-to-end workflow | The repository's address as a link over its screenshot; the skills you type and the skills they call; the install command |
| 29 | 30:10 | Classic practice, adapted for agents | Six books from 1999 to 2018, the idea the skills take from each and the skills that carry it, user stories for the spec among them; the speaker notes add the README's "Why These Skills Exist" section on five pages of their own |
| 30 | 31:20 | Pocock's flow: who does what | Person, agent and output across the five stages: spec-driven, then test-first |
| 31 | 32:30 | A /grill-with-docs session | Example session on the short request: numbered markers for a looked-up fact, a recommended answer and the ADR decision; an arrow to the glossary entry it adds |
| 32 | 33:50 | The specimen split, stage by stage | What each stage produces for the specimen split, under the columns of slide 30 |
| 33 | 35:00 | How /implement uses /tdd | The five steps of a run; rules of the /tdd loop |
| 34 | 36:10 | When is the full flow worth it? | Size and meaning of a change decide the route |
| — | 36:50 | Divider 08: A realistic starting point | |
| 35 | 37:00 | Other skill packages | Pocock's skills, superpowers and andrej-karpathy-skills: who made each, what it is, its steps and its rule for tests; in all three the check is set before the code |
| 36 | 38:00 | Checklist for your repository | Groundwork, context and workflow: a workflow that suits you, such as Pocock's skills, your own skills for the tasks you repeat, tests agreed first, a worktree or forked session per task, and your own review |
| — | 38:50 | Thank you | The title slide's layout with the thanks in place of the title; the speaker notes keep four questions to open the discussion |

## Appendix

A1 `AGENTS.md` template; A2 glossary, coding-standards and ADR templates; A3 the upgrade: uv, and A4 conda or uv?, both kept for questions after slide 6, with notes that start "If asked"; A5 how Codex finds instruction files; A6 Pocock's workflow in the July 2026 video and in v1.3.1; A7 to A10 references, A10 for the books behind Pocock's skills and the other skill packages.
