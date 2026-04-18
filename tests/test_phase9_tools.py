import unittest
from pathlib import Path


class Phase9ToolingTests(unittest.TestCase):
    def test_tool_scripts_exist(self):
        self.assertTrue(Path("tools/inspect_task.py").exists())
        self.assertTrue(Path("tools/replay_audit.py").exists())
        self.assertTrue(Path("tools/list_known_issues.py").exists())

    def test_known_issues_exists(self):
        self.assertTrue(Path("docs/KNOWN_ISSUES.md").exists())


if __name__ == "__main__":
    unittest.main()
