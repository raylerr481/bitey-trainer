import unittest

from trainer import MockProvider, evaluate


class TrainerSmokeTest(unittest.TestCase):
    def test_smoke_evaluation(self):
        result = evaluate(MockProvider(), "Explain what Bitey Trainer does.")
        self.assertTrue(result.passed)
        self.assertEqual(result.score, 1.0)
        self.assertIn("Bitey Trainer", result.response)


if __name__ == "__main__":
    unittest.main()
