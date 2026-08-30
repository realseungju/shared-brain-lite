# Conventions

한국어 번역: [`conventions.ko.md`](conventions.ko.md)

## Filenames

| Location | Format |
|---|---|
| `tasks/*/` | `TYYYY-MM-DD-{slug}.md` |
| `system/sessions/` | `YYYY-MM-DD-{slug}.md` |
| `specs/` | `{slug}.md` |
| `knowledge/` | `{slug}.md` |
| `research/` | `{project-slug}/{doc-slug}.md` |
| `inbox/` | `YYYYMMDD-{source}-{slug}.md` |

A slug uses lowercase letters, digits, and hyphens only. Template files whose name starts
with `_template.md` are the exception.

## Task frontmatter

`infra/new-task.py` creates it and `infra/brain-lint.py` checks it. When you move a task
between states by hand, you fill these in yourself.

| Field | Required when | Value |
|---|---|---|
| `id` | Always | Exactly the filename without the extension |
| `title` | Always | One-line title |
| `phase` | Always | `planning` \| `review` \| `implementation` \| `validation` |
| `assignee_role` | Optional | The role responsible, not a person's name |
| `spec` | Optional | The linked `specs/{slug}.md`, or `none` |
| `agent` | In `doing/` | The writer currently holding this task |
| `started` | In `doing/` | `YYYY-MM-DD` |
| `finished` | In `done/` | `YYYY-MM-DD` |
| `closed_reason` | In `done/` | `completed` \| `cancelled` \| `superseded` |
| `result` | In `done/` | A commit hash, PR number, or other checkable artifact |

`phase` is **which stage the task is at**; `backlog/doing/done` is **which directory it is
in**. They are independent — a `planning` task sitting in `doing/` is normal.

## Task states

```text
backlog → doing → done
```

Closing reasons:

- `completed`: the goal was reached
- `cancelled`: stopped with no plan to resume
- `superseded`: replaced by a different approach

## Session frontmatter

`infra/new-session.py` creates it. Do not create one by hand.

| Field | Value |
|---|---|
| `date` | `YYYY-MM-DD` — must match the first part of the filename |
| `agent` | The writer's name |
| `slug` | Must match the rest of the filename |
| `tags` | A list of lowercase-hyphen tags |

The body must contain a `## What was done` section and an `## Open and next` section — both
are checked by lint. `## Decisions and why` and `## Cautions` are written by the generator
but not enforced. Every session file must have a one-line entry in
`system/sessions/index.md`; the generator adds it, so this only matters if you delete a
file.

## Commits

Conventional Commits are recommended.

```text
<type>(<scope>): <imperative summary>
```

## Documents

- State the conclusion first.
- Do not copy the same content into several documents.
- Keep current state and reusable knowledge apart.
- Leave what the next agent needs, and no more.
