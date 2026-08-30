---
id: T2026-07-28-research-conventions
title: Minimal research/ conventions and templates
phase: implementation
assignee_role: maintainer
spec: none
agent: Claude (Opus 5)
started: 2026-07-28
finished: 2026-07-28
closed_reason: completed
result: 683bbb1
---

# Minimal research/ conventions and templates

## Purpose

Let someone who takes this repository over for research start recording on day one.
`research/` used to be an empty extension point, which left the main use case empty.

## To do

- [x] `research/README.md` — directory layout, canonical-document rule, reproducibility rule
- [x] `research/_template/overview.md` — project overview template
- [x] `research/_template/experiment.md` — experiment record template (falsification
      condition, pinned settings, kind of evidence)
- [x] Add a Research section to `system/RULES.md` and drop `research/` from optional areas
- [x] Add `research/` to the filename table in `system/conventions.md`
- [x] Record "conventions only, no automation" as ADR-001

## Done when

- [x] Tier 0 reading cost does not grow (research is Tier 2)
- [x] `brain-lint` does not inspect the contents of `research/`
- [x] A new project document can be started from the templates alone

## Notes

The reason for not enforcing it is in ADR-001. Research records differ too much between
projects; enforcing a structure produces workarounds, and workarounds erode trust in every
rule.
