import unittest
from opportunity_matcher import Opportunity, score_opportunity
from profile import PRIMARY_PROFILE


class MatchingTest(unittest.TestCase):
    def test_human_data_evaluation_match(self):
        opportunity = Opportunity(
            title="AI Response Evaluator",
            mode="HUMAN",
            skills=["data entry", "Microsoft Excel", "QA", "structured feedback"],
            languages={"English": "intermediate"},
            human_required=True,
        )
        score, reasons = score_opportunity(opportunity, PRIMARY_PROFILE)
        self.assertGreaterEqual(score, 70)
        self.assertTrue(reasons)

    def test_bitey_agent_opportunity(self):
        opportunity = Opportunity(
            title="AI Dataset Processing Agent",
            mode="BITEY",
            skills=["Python", "APIs"],
            languages={},
            agent_allowed=True,
        )
        score, reasons = score_opportunity(opportunity, PRIMARY_PROFILE)
        self.assertGreaterEqual(score, 50)
        self.assertIn("agent execution permitted", reasons)


if __name__ == "__main__":
    unittest.main()
