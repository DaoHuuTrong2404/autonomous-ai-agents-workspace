import unittest

from agents.cua_vision import VisionCUAAgent
from agents.hybrid_rag import HybridRAG


class UIRegressionTests(unittest.TestCase):
    def test_skips_non_interactive_label_match(self):
        agent = VisionCUAAgent()
        agent.parse_mock_som([
            {"label": "Save heading", "interactive": False, "bbox": [0, 0, 10, 10]},
            {"label": "Save button", "interactive": True, "bbox": [20, 20, 40, 40]},
        ])
        action = agent.click_element_by_label("save")
        self.assertEqual(action["target_id"], 2)
        self.assertEqual(action["coordinates"], (30, 30))
        self.assertEqual(action["status"], "SIMULATED")

    def test_non_interactive_only_does_not_record_click(self):
        agent = VisionCUAAgent()
        agent.parse_mock_som([{"label": "Save", "interactive": False}])
        self.assertIsNone(agent.click_element_by_label("Save"))
        self.assertEqual(agent.action_history, [])

    def test_blank_query_does_not_choose_arbitrary_element(self):
        agent = VisionCUAAgent()
        agent.parse_mock_som([{"label": "Delete"}])
        for label in ("", "   "):
            self.assertIsNone(agent.click_element_by_label(label))
        self.assertEqual(agent.action_history, [])


class RetrievalRegressionTests(unittest.TestCase):
    def setUp(self):
        self.search = HybridRAG()
        self.search.add_document("one", "agent tools")
        self.search.add_document("two", "agent")

    def test_zero_limit_returns_no_hits(self):
        self.assertEqual(self.search.search("agent", top_k=0), [])

    def test_invalid_limits_raise_even_for_empty_corpus(self):
        for search in (self.search, HybridRAG()):
            for limit in (-1, 1.5, True, "2", None):
                with self.subTest(limit=limit):
                    with self.assertRaises(ValueError):
                        search.search("agent", top_k=limit)

    def test_empty_and_unmatched_queries(self):
        for query in ("", "  ", "unmatched"):
            self.assertEqual(self.search.search(query), [])

    def test_limit_and_ranking(self):
        hits = self.search.search("tools", top_k=1)
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["id"], "one")


if __name__ == "__main__":
    unittest.main()
