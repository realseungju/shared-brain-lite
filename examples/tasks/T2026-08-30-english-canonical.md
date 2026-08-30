---
id: T2026-08-30-english-canonical
title: English as the canonical language
phase: implementation
assignee_role: maintainer / agent
spec: specs/english-canonical.md
agent: Claude (Opus 5)
started: 2026-08-30
finished: 2026-08-30
closed_reason: completed
result: fb134ea
---

# English as the canonical language

Spec: [`specs/english-canonical.md`](../../specs/english-canonical.md)

Five layers move together. Doing fewer than all five leaves the rules and the generators
disagreeing with each other.

## To do

- [x] Layer 1 — entry stubs: `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`,
      `.github/copilot-instructions.md`
- [x] Layer 2 — `system/RULES.md`, `system/conventions.md` to English;
      `system/RULES.ko.md`, `system/conventions.ko.md` as translations with a canonical
      pointer and synced-from commit
- [x] Layer 3 — `infra/new-session.py`, `infra/new-task.py`: emitted section headings and
      CLI text
- [x] Layer 4 — `infra/brain-lint.py`: enforced section constants and every message
- [x] Layer 5 — `infra/tests/*` assertions, `examples/` rewritten against the English schema
- [x] `system/context.md` placeholder and `system/sessions/index.md` header
- [x] Verify: full test suite, `brain-lint`, a generated session and task, CI

## Done when

- Test count is not lower than 21 and all pass
- `brain-lint` is clean and prints English
- Both `.ko.md` siblings exist with a canonical pointer and a synced-from commit
- CI green

## Notes

- 2026-08-30 planned. Measured that the Korean is not decoration: `new-session.py` emits
  `## 한 것` / `## 결정·이유` / `## 미완·다음` / `## 주의·함정` and `brain-lint.py` enforces
  those exact strings, with 16 test assertions and 2 example files pinned to them. This is
  a schema change.
- 2026-08-30 the window is now: 0 forks, 0 stars, 0 watchers, 0 open issues
  `[measured: gh api, 2026-08-30]`. The only downstream is `shared-brain-research`, owned by
  the same author. One adopter and this becomes permanent.
- Adding lint checks and propagating to `shared-brain-research` are deliberately out of
  scope — both wait on decisions recorded elsewhere.

- 2026-08-30 done. All five layers landed in `fb134ea`; `1873c1d` filled in the
  synced-from commit for the two translations. Verified: 21 tests pass (unchanged in
  count), `brain-lint` clean and printing English, a generated task and session pass lint
  with English headings. Residue recorded in ADR-003: templates under `research/`,
  `skills/`, `knowledge/`, `inbox/`, and `tasks/` are still Korean.
