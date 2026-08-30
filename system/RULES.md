# RULES — Shared Brain Lite

**Work that isn't written down cannot reach the next agent.**

한국어 번역: [`RULES.ko.md`](RULES.ko.md)

## Starting a session

1. Read this file.
2. Read `system/context.md`.
3. Read the last 3-5 lines of `system/sessions/index.md`.
4. Look at the filenames in `tasks/doing/` — filenames only.
5. Read only the task and spec connected to the work at hand.

Do not read the whole repository every session.

## Reading tiers

| Tier | When | What |
|---|---|---|
| 0 | Every session | `context.md`, the tail of the session index, filenames in `doing/` |
| 1 | Starting a task | That task and the spec it links to |
| 2 | Only when needed | ADRs, knowledge, research, past sessions |

## Workflow

```text
inbox → planning/spec → tasks/backlog → tasks/doing → tasks/done
```

- `inbox/` is for capturing ideas. Do not implement straight from it.
- Write the requirements and the done condition into a spec or a task before building.
- When a task starts, move it to `doing/` and fill in `agent` and `started`.
- When it finishes, move it to `done/` and fill in `finished`, `closed_reason`, `result`.
- One task has one active writer.

Field names and allowed values are all in `system/conventions.md`. `brain-lint` rejects a
file that leaves them out, so read the table instead of guessing.

## Creating files

Task and session files are never created by hand.

```sh
python infra/new-task.py {slug} --title "Title"
python infra/new-session.py {slug} --agent {name} --tags {tags} \
  --hook "One line the next agent reads to decide whether to open this" \
  --did "What was done" --next "What is next"
```

Filling in the body of a generated task or session afterwards is expected.

## Closing a session

Leave a session summary if the next agent needs to know about the work.

- Unfinished work belongs in a task, not in the summary.
- Changes to the current state go into `system/context.md`.
- Reusable lessons are promoted to `knowledge/`.
- A typo fix or a wording change can skip the task and the session summary.

## Research records

Research and experiment records live in `research/{project-slug}/`. Conventions and
templates are in `research/README.md`.

- One `overview.md` per project; split the rest by topic.
- **Name one canonical document** and keep the conclusions only there. Execution logs are a
  separate document.
- Research is Tier 2. It is not read during the start procedure — open it when needed.
- Raw data, model weights, and secrets do not go in Git. Record where they are instead.

## Optional areas

`personal/` is an extension point with no behaviour by default. Do not invent a file
layout, automation, or data format for it before the user asks for a real use case.

## Prohibited

- Building a feature with no spec and no done condition
- Creating a task or session file without the generator
- Recording an unverified result as complete
- Committing real personal data, tokens, or secrets to a public repository
- Storing large datasets or model files directly in Git
