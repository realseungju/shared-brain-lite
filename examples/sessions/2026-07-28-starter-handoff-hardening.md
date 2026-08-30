---
date: 2026-07-28
agent: Claude (Opus 5)
slug: starter-handoff-hardening
tags: [starter, research, onboarding, lint, portability]
---

# 2026-07-28 — Claude (Opus 5) — starter-handoff-hardening

## What was done

Reviewed the first Codex draft and hardened it against two goals: handing the repository to
a fellow researcher, and publishing it. The draft was green on structure, tests, and CI,
with zero personal data leaked. The problem was that it did not match those goals.

- **Introduced `research/`** — the recipient is a researcher, yet the research-record module
  was empty under a "do not build before it is requested" rule. Added README conventions and
  overview/experiment templates, but no automation (ADR-001).
- **English README** — the biggest bottleneck for publishing. Korean moved to `README.ko.md`.
- **Fixed a quick start that failed its own gate** — following the three steps and moving a
  task into `doing/` made lint reject it twice for a missing `agent` and `started`. The
  guidance was in RULES but not in the README.
- **Documented the lint schema** — the four valid `phase` values, `assignee_role`, `spec`,
  session frontmatter, and the required sections existed only in code. That is a hole that
  contradicts a discipline of reading Tier 0 only.
- **Hook portability** — a hardcoded `python` dies instantly on macOS and most Linux. The
  hook now searches for an interpreter that actually runs.
- **`sessions/index.md merge=union`** — an append-only log conflicts deterministically when
  two people close a session.
- **Tests 6 → 18** — done fields, phase values, duplicate ids, session sections, index
  consistency, and whether generator output passes lint (if the generator and the checker
  disagree, the whole discipline collapses).
- **Example artifacts** — two ADRs, one closed task, and this session, so a visitor can see
  the shape of the records without cloning.

## Decisions and why

`research/` ships conventions and templates only, with no automation (ADR-001). `personal/`
stays empty until it is requested (ADR-002).

## Open and next

Collect feedback from a colleague, then decide whether to start `personal/`.

## Cautions

Picking an interpreter in the pre-commit hook by checking only that `command -v python3`
*exists* dies on Windows with exit 49, because it finds the Microsoft Store install stub. A
fix aimed at macOS broke Windows, and it would have shipped if the hook had never actually
been run. **A candidate must be judged by whether it runs, not by whether it exists** —
`"$candidate" -c "import sys"`.

The general form of the same trap: a gate that is *installed* is not a gate that *runs*. So
the README does not stop at hook installation; it also tells you to confirm the hook fires
with `git commit --allow-empty`.
