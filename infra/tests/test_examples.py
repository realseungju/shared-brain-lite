"""Keep the artifacts in examples/ satisfying the real schema.

brain-lint does not inspect examples/ — that is what lets the live tree ship empty.
So when the schema changes, only the examples rot, silently. Here we drop them into
their real places in an empty repository and run lint to catch that drift.
"""
from __future__ import annotations

from pathlib import Path
import shutil
import tempfile
import unittest

from support import REPO, make_brain, run_script, write

EXAMPLES = REPO / "examples"


class ExampleArtifactTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        make_brain(self.root)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_examples_directory_is_not_empty(self) -> None:
        self.assertTrue(sorted(EXAMPLES.glob("sessions/*.md")), "no example session")
        self.assertTrue(sorted(EXAMPLES.glob("tasks/*.md")), "no example task")

    def test_examples_pass_lint_in_place(self) -> None:
        index_lines = []
        for path in sorted(EXAMPLES.glob("sessions/*.md")):
            shutil.copy(path, self.root / "system/sessions" / path.name)
            index_lines.append(f"- [{path.stem}]({path.name}) — example")
        write(
            self.root / "system/sessions/index.md",
            "# Sessions Index\n\n" + "\n".join(index_lines) + "\n",
        )
        for path in sorted(EXAMPLES.glob("tasks/*.md")):
            shutil.copy(path, self.root / "tasks/done" / path.name)

        result = run_script("brain-lint.py", str(self.root))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_live_tree_ships_empty(self) -> None:
        """Shipping state — a template cloner must not inherit someone else's records."""
        sessions = sorted(
            p for p in (REPO / "system/sessions").glob("*.md") if p.name != "index.md"
        )
        self.assertEqual(sessions, [], f"live sessions left behind: {sessions}")
        done = sorted((REPO / "tasks/done").glob("*.md"))
        self.assertEqual(done, [], f"live done tasks left behind: {done}")


if __name__ == "__main__":
    unittest.main()
