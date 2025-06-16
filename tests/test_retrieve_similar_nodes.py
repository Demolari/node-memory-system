import unittest
from tools import retrieve_similar_nodes


class TestRetriever(unittest.TestCase):
    def test_retrieve_returns_list(self):
        results = retrieve_similar_nodes.retrieve_similar_nodes("example query", top_k=2)
        self.assertIsInstance(results, list)
        self.assertLessEqual(len(results), 2)

    def test_results_format(self):
        results = retrieve_similar_nodes.retrieve_similar_nodes("test query", top_k=1)
        for node_id, score in results:
            self.assertIsInstance(node_id, str)
            self.assertIsInstance(score, float)


if __name__ == "__main__":
    unittest.main()