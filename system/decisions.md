# Decisions

Record an important decision by adding an ADR below, without deleting what is already
there. Reversing a decision is also an addition, not a deletion — why it changed matters as
much as the decision itself.

```markdown
## ADR-000: Decision title
- Date: YYYY-MM-DD
- Status: proposed | accepted | superseded
- Decision:
- Rationale:
- Consequences:
```

---

## ADR-001: research/ ships conventions and templates only, with no automation
- Date: 2026-07-28
- Status: accepted
- Decision: Ship the `research/{project-slug}/overview.md` layout and an experiment-record
  template. Do not add generators, lint checks, or index automation for them.
- Rationale: Research records differ enormously between projects. Enforcing a structure
  makes people work around it in the projects it does not fit, and once the working around
  starts, trust in every other rule erodes with it. What does pay regardless of shape is
  "one canonical document, execution logs separate from conclusions, state the kind of
  evidence, keep reproduction information." Enforcement is reserved for the things that are
  *lost* if the next person cannot find them, like tasks and sessions.
- Consequences: research stays Tier 2, so the start procedure does not get more expensive.
  `brain-lint` checks only that `research/` exists, never its contents.

## ADR-002: `personal/` stays empty until it is requested
- Date: 2026-07-28
- Status: accepted
- Decision: Do not build a structure for personal schedules or idea management. Leave it as
  an extension point, and record the conditions for starting it in an opt-in task in
  `tasks/backlog/`.
- Rationale: Personal habits differ from person to person, and a structure nobody uses is
  pure reading cost. It is also a route by which personal data ends up in a public
  repository.
- Consequences: If it is ever needed, it starts from planning. Until then the default
  distribution keeps a small surface.

## ADR-003: English is canonical; Korean ships as a sibling translation
- Date: 2026-08-30
- Status: accepted
- Decision: English is the canonical language for the path an agent and a cloner actually
  walk — the four entry stubs, `system/RULES.md`, `system/conventions.md`, the section
  headings the generators emit, every `brain-lint` message, the tests, `examples/`,
  `system/context.md`, and `system/decisions.md`. Korean is preserved as
  `system/RULES.ko.md` and `system/conventions.ko.md`, each opening with a pointer to the
  canonical file and the commit it was synced from.
- Rationale:
  - The intent was already English-first, but it had reached exactly one file. `README.md`
    was English while the four entry stubs an agent reads *before* it were Korean, as was
    `system/RULES.md` that those stubs point at.
  - This is not a translation, it is a schema change. `new-session.py` emitted `## 한 것`,
    `## 결정·이유`, `## 미완·다음`, `## 주의·함정`, and `brain-lint.py` held those exact
    Korean strings as the constants it enforced, with 16 test assertions and two example
    files pinned to them. Translating the rules without the generators would have left
    `RULES.md` describing a session summary the generator then wrote in Korean.
  - The window is now. Measured 2026-08-30: 0 forks, 0 stars, 0 watchers, 0 open issues.
    The only downstream is `shared-brain-research`, owned by the same author. The cost of a
    breaking schema change is exactly zero today and becomes permanent with one adopter.
  - No parity gate between a file and its `.ko.md` sibling. A lint can check that a
    translation exists and which commit it claims to follow; it cannot honestly check that
    the meaning still matches. Item 3 of the spec makes the lag visible instead of
    pretending to prevent it.
- Consequences:
  - A Korean reader follows `RULES.ko.md` and `conventions.ko.md`, and the canonical pointer
    tells them when the translation is behind.
  - Templates under `research/`, `skills/`, `knowledge/`, `inbox/`, and `tasks/` are still
    Korean. That is a known residue, deliberately left for a later pass.
  - `shared-brain-research` is downstream and is not touched here. It picks this up through
    the `UPSTREAM.md` procedure, selectively, on its own schedule.
  - Spec: `specs/english-canonical.md`. Task: `T2026-08-30-english-canonical`.
