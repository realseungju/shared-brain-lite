# Shared Brain Lite

A lightweight starter for using a Git repository as **shared long-term memory across AI agents**.

한국어 문서: [README.ko.md](README.ko.md)

Chat sessions forget. Different tools — Claude, Codex, Gemini, Copilot — don't share memory
with each other. This repo makes the *repository* the memory instead: plain Markdown, one
entry point every tool reads, and a lint gate that keeps the records honest.

```text
capture → plan/spec → task → work → session summary → next agent
```

## Why this instead of a notes folder

Free-form notes rot because nothing enforces them. Three mechanisms keep this from rotting:

- **Tiered reading.** An agent reads `system/RULES.md`, `system/context.md`, the last few
  lines of the session index, and the filenames in `tasks/doing/` — nothing else, until a
  specific task needs it. Onboarding cost stays flat as the repo grows.
- **Generators, not hand-editing.** Task and session files are created by scripts, so every
  record has the same frontmatter schema and lands in the right place.
- **A lint gate.** `brain-lint.py` runs on pre-commit and in CI. A session with no index
  entry, a task in `done/` with no result, a task id that disagrees with its filename — all
  rejected. Structure that isn't checked is structure that quietly stops being true.

## Quick start

Requirements: Git and Python 3.10+. No third-party packages.

1. Describe your actual work in `system/context.md`.
2. Create your first task:

```sh
python infra/new-task.py first-task --title "My first task"
```

3. Fill in the generated file in `tasks/backlog/`. When you start it, move it to
   `tasks/doing/` **and fill in the `agent` and `started` fields** — `brain-lint` requires
   them, and the pre-commit hook will reject the commit otherwise. Field names and allowed
   values are in [`system/conventions.md`](system/conventions.md).
4. When you stop working, write a session summary:

```sh
python infra/new-session.py first-session \
  --agent Codex \
  --tags demo \
  --hook "One line the next agent reads to decide whether to open this" \
  --did "Created the first task and checked the structure" \
  --next "Write the real project context"
```

5. Check the structure:

```sh
python infra/brain-lint.py
python -m unittest discover -s infra/tests -v
```

## Layout

```text
system/       rules, current context, session summaries, ADRs
tasks/        backlog / doing / done
specs/        what to build, before building it
inbox/        captured ideas, not yet planned
knowledge/    reusable lessons that outlive a single project
research/     per-project research notes and experiment records (Tier 2)
skills/       extension point for tool-specific skills
personal/     extension point, empty by default
infra/        generators, lint, tests, Git hook
```

`system/RULES.md` is the single source of operating rules. `CLAUDE.md`, `AGENTS.md`,
`GEMINI.md`, and `.github/copilot-instructions.md` are thin stubs that all point at it, so
adding a new AI tool means adding one more stub — not one more copy of the rules.

## Included

- Shared entry points for Claude, Codex, Gemini, and Copilot
- Tier 0/1/2 reading discipline
- `inbox → spec → task` planning gate
- `backlog → doing → done` task lifecycle
- Session summaries with tags, hooks, and an append-only index
- Task and session generators
- `brain-lint` structural checks, wired into pre-commit and GitHub Actions
- Templates for specs, knowledge nodes, research notes, and experiment records

## Not included

- Personal calendar / idea management (`personal/` is a deliberate blank — see ADR-002)
- External calendar or GitHub Issue sync
- Multi-worktree auto-integration
- Model routing, evaluation harnesses, or agent safety hooks

These were left out on purpose. See `system/decisions.md` for the reasoning, and
`tasks/backlog/` for the opt-in task to add them if you actually need them.

## Git hook

Optional but recommended. Runs `brain-lint` before every commit:

```sh
git config core.hooksPath infra/hooks
```

Verify it actually fires — a gate you believe in but that never runs is worse than no gate:

```sh
git commit --allow-empty -m "hook check"   # should print "brain-lint: 클린 ✓"
```

GitHub Actions runs the same lint and the test suite on every push and PR, so CI catches it
even if the local hook is missing.

## Working with someone else

Each person can keep their own copy, or you can share one repo. If you share one, note that
`system/sessions/index.md` is append-only and will conflict whenever two people close a
session — `.gitattributes` already sets `merge=union` on it, which keeps both sides' lines.
Task and session bodies are one-item-per-file, so they don't conflict.

## Principles

- Work that isn't written down doesn't exist for the next agent.
- Read the tier you need, not the whole repo.
- Don't implement an inbox item before it becomes a spec or a task.
- Never commit real secrets, personal data, or large research artifacts to a public repo.

## License

MIT — see [LICENSE](LICENSE).
