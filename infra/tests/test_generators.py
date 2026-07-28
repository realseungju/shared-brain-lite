from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from support import make_brain, run_script


class GeneratorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        make_brain(self.root)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_new_task_creates_date_slug_task(self) -> None:
        result = run_script(
            "new-task.py",
            "first-task",
            "--title",
            "첫 작업",
            "--date",
            "2026-07-28",
            "--root",
            str(self.root),
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        path = self.root / "tasks/backlog/T2026-07-28-first-task.md"
        self.assertTrue(path.is_file())
        self.assertIn("title: 첫 작업", path.read_text(encoding="utf-8"))

    def test_new_task_rejects_invalid_slug(self) -> None:
        result = run_script(
            "new-task.py",
            "Bad Slug",
            "--title",
            "실패",
            "--root",
            str(self.root),
        )
        self.assertEqual(result.returncode, 2)

    def test_new_session_creates_file_and_index_entry(self) -> None:
        result = run_script(
            "new-session.py",
            "first-session",
            "--agent",
            "Codex",
            "--tags",
            "demo,lite",
            "--hook",
            "첫 session",
            "--did",
            "생성기 검증",
            "--next",
            "다음 작업",
            "--date",
            "2026-07-28",
            "--root",
            str(self.root),
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        path = self.root / "system/sessions/2026-07-28-first-session.md"
        self.assertTrue(path.is_file())
        index = (self.root / "system/sessions/index.md").read_text(encoding="utf-8")
        self.assertIn(path.name, index)


if __name__ == "__main__":
    unittest.main()
