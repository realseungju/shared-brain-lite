# Examples

**These are for reading. Nothing here is a live record.**

Shipping a filled `system/sessions/` and `tasks/done/` would drop someone else's records
straight into the Tier 0 of anyone who clones this template. So the real artifacts live here
purely to show their shape, and the live tree ships empty.

| File | What |
|---|---|
| `sessions/2026-07-28-starter-handoff-hardening.md` | A filled session summary — the four sections: what was done, decisions, open items, cautions |
| `tasks/T2026-07-28-research-conventions.md` | A closed task — every field you fill in when moving to `done/` |
| `tasks/T2026-08-30-english-canonical.md` | A closed task with a linked spec — see `specs/english-canonical.md` and ADR-003 |

## Cautions

- **`result:` values here (`683bbb1`, `fb134ea`) are commit hashes from this repository's
  own history.** They do not exist in the history of a repository created from the
  template. Read them as format examples only.
- Do not copy these files to start your own. Use the generators:

```sh
python infra/new-task.py {slug} --title "Title"
python infra/new-session.py {slug} --agent {name} --tags {tags} \
  --hook "One line for the index" --did "What was done" --next "What is next"
```

- `brain-lint` does not inspect `examples/`. Instead a regression test drops these files
  into an empty repository and checks that lint passes, so a schema change breaks the
  examples visibly (`infra/tests/test_examples.py`).
