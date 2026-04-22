import unittest
from pathlib import Path


class Phase11UISkeletonTests(unittest.TestCase):
    def test_ui_files_exist(self):
        self.assertTrue(Path("ui/index.html").exists())
        self.assertTrue(Path("ui/styles.css").exists())
        self.assertTrue(Path("ui/mock-api.js").exists())
        self.assertTrue(Path("ui/app.js").exists())

    def test_index_contains_navigation_shell(self):
        content = Path("ui/index.html").read_text(encoding="utf-8")
        self.assertIn("DeafPiper Console", content)
        self.assertIn('data-view="dashboard"', content)
        self.assertIn('data-view="task-detail"', content)
        self.assertIn('data-view="candidate-review"', content)
        self.assertIn('data-view="dead-end-center"', content)
        self.assertIn('data-view="budget-provider"', content)


if __name__ == "__main__":
    unittest.main()
