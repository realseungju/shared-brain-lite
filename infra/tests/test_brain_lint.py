from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from support import make_brain, run_script, write


class BrainLintTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        make_brain(self.root)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def lint(self):
        return run_script("brain-lint.py", str(self.root))

    def test_minimal_brain_is_clean(self) -> None:
        result = self.lint()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_task_requires_matching_id(self) -> None:
        write(
            self.root / "tasks/backlog/T2026-07-28-example.md",
            """---
id: T2026-07-28-wrong
title: 예제
phase: planning
---
""",
        )
        result = self.lint()
        self.assertEqual(result.returncode, 1)
        self.assertIn("id와 파일명 불일치", result.stdout)

    def test_session_requires_index_entry(self) -> None:
        write(
            self.root / "system/sessions/2026-07-28-example.md",
            """---
date: 2026-07-28
agent: Codex
slug: example
tags: [demo]
---

## 한 것

완료

## 미완·다음

없음
""",
        )
        result = self.lint()
        self.assertEqual(result.returncode, 1)
        self.assertIn("index 미등재", result.stdout)


if __name__ == "__main__":
    unittest.main()
