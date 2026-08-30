# Changelog

All notable changes to this project are recorded here. The reasoning behind a decision
lives in `system/decisions.md`; this file records what changed and when.

This project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html). A change to
the record schema — frontmatter fields, enforced section headings, generator output — is a
breaking change.

## [Unreleased]

## [0.1.0] — 2026-08-30

First tagged release. The starter has been in use since 2026-07-28; this marks the point at
which its operating path is English and its schema is settled.

### Changed

- **BREAKING — English is the canonical language of the operating path** (ADR-003). The four
  entry stubs, `system/RULES.md`, `system/conventions.md`, `system/context.md`,
  `system/decisions.md`, every `brain-lint` message, and the section headings the generators
  emit are now English.
- **BREAKING — session section headings renamed.** `## 한 것` → `## What was done`,
  `## 결정·이유` → `## Decisions and why`, `## 미완·다음` → `## Open and next`,
  `## 주의·함정` → `## Cautions`. `brain-lint` enforces the first and third. Task headings
  become `## To do`, `## Done when`, `## Notes`. A repository created from an earlier copy
  of this template must rename these headings in its existing session files.
- `examples/` rewritten against the English schema, so `test_examples` keeps proving the
  examples match what lint enforces.

### Added

- `system/RULES.ko.md` and `system/conventions.ko.md` — Korean translations, each naming the
  canonical file and the commit it was synced from.
- `specs/english-canonical.md` and ADR-003.
- This changelog.

### Notes

- Document bodies may be written in any language. Only the headings and the frontmatter are
  fixed.
- 21 regression tests pass and `brain-lint` is clean, unchanged in count from before.

## [0.0.0] — 2026-07-28

Initial public starter: tiered reading, task and session generators, `brain-lint` on
pre-commit and in CI, isolated `examples/`, an empty live tree, and templates for specs,
knowledge nodes, research notes, and experiment records.
