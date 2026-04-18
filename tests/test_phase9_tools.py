import unittest
from pathlib import Path


class Phase9ToolingTests(unittest.TestCase):
    def test_tool_scripts_exist(self):
        self.assertTrue(Path("deafpiper_tool.py").exists())
        self.assertTrue(Path("tools/inspect_task.py").exists())
        self.assertTrue(Path("tools/replay_audit.py").exists())
        self.assertTrue(Path("tools/list_known_issues.py").exists())

    def test_known_issues_exists(self):
        self.assertTrue(Path("docs/KNOWN_ISSUES.md").exists())

    def test_pipeline_prototype_directory_absent(self):
        self.assertFalse(Path("pipeline").exists())

    def test_pipeline_assets_merged_to_root(self):
        self.assertTrue(Path("README.md").exists())
        self.assertTrue(Path("playbook/00_START_HERE.md").exists())
        self.assertTrue(Path("templates/PRD.json").exists())
        self.assertTrue(Path("gpt_configs/01_SETUP_PROMPTING.json").exists())


if __name__ == "__main__":
    unittest.main()
