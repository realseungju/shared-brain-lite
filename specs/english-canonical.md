---
feature: english-canonical
status: approved
author: Claude (Opus 5)
date: 2026-08-30
related_tasks: [T2026-08-30-english-canonical]
---

# English as the canonical language

## Purpose

The README is in English, but everything an agent or a cloner touches *after* it is Korean:
the four entry stubs (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`,
`.github/copilot-instructions.md`), `system/RULES.md`, `system/conventions.md`, the section
headings the generators emit, and every `brain-lint` message.

The intent was already English-first — it only reached one file. This spec propagates it to
the path an agent actually walks.

## The scope is a schema change, not a translation

`new-session.py` emits `## 한 것`, `## 결정·이유`, `## 미완·다음`, `## 주의·함정`, and
`brain-lint.py` holds those Korean headings as the constants it enforces. Translating the
rules without the generators would leave `RULES.md` telling an agent to write a session
summary that the generator then writes in Korean. Five layers move together or none do:

| Layer | Files |
|---|---|
| 1 | entry stubs ×4 |
| 2 | `system/RULES.md`, `system/conventions.md` |
| 3 | `infra/new-session.py`, `infra/new-task.py` — including emitted section headings |
| 4 | `infra/brain-lint.py` — enforced constants and messages |
| 5 | `infra/tests/*` assertions, `examples/` |

## Why now

Measured 2026-08-30: 0 forks, 0 stars, 0 watchers, 0 open issues. The only downstream is
`shared-brain-research`, which the same author owns. The cost of a breaking schema change
is exactly zero right now and becomes permanent the moment one adopter exists.

## Requirements

1. English is canonical for the five layers above.
2. Korean is preserved as a sibling translation: `system/RULES.ko.md`,
   `system/conventions.ko.md` — the pattern `README.md` / `README.ko.md` already uses.
3. Each `.ko.md` file opens with a canonical pointer and the commit it was synced from, in
   the same idiom `UPSTREAM.md` uses for its imported commit. A translation is allowed to
   lag; it is not allowed to lie about being current.
4. Entry stubs stay English-only. They are pointers, not documents.
5. `brain-lint` and generator output are English. Test assertions follow.
6. `examples/` is rewritten against the English schema so `test_examples` keeps proving the
   examples match what `brain-lint` enforces.
7. No behaviour change. The checks that pass today pass after, and the test count does not
   drop.

## Non-goals

- Translating `research/`, `skills/`, `knowledge/`, `inbox/`, `tasks/` templates. Later.
- Adding new lint checks. That decision waits on the product-line question.
- Touching `shared-brain-research`. Propagation happens through `UPSTREAM.md` afterwards.
- A machine-checked parity gate between a file and its `.ko.md` sibling. Item 3 makes the
  lag visible; enforcing semantic parity is not something a lint can do honestly.

## Done when

- [ ] The five layers are English and `python -m unittest discover -s infra/tests` reports
      no fewer than 21 tests, all passing.
- [ ] `python infra/brain-lint.py` is clean and prints English.
- [ ] `system/RULES.ko.md` and `system/conventions.ko.md` exist, each with a canonical
      pointer and a synced-from commit.
- [ ] A fresh session and task created by the generators pass lint with English headings.
- [ ] CI is green.
