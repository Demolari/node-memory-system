import unittest
from tools import retrieve_similar_nodes
from tools.retrieve_similar_nodes import retrieve_similar_nodes

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

#poprawić to co tu najebałem

class TestRetrieveSimilarNodesMock(unittest.TestCase):
    def setUp(self):
        self.embeddings_dict = {
            "node1": [0.1, 0.2, 0.3],
            "node2": [0.15, 0.25, 0.35],
            "node3": [0.9, 0.8, 0.7]
        }

    def test_similar_nodes(self):
        query_vector = [0.14, 0.26, 0.36]
        result = retrieve_similar_nodes(query_vector, self.embeddings_dict, top_k=2)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0][0], "node2")
        self.assertIn("node1", [r[0] for r in result])

    def test_empty_embeddings(self):
        result = retrieve_similar_nodes([0.1, 0.2, 0.3], {}, top_k=2)
        self.assertEqual(result, [])

    def test_insufficient_nodes(self):
        small_dict = {"node1": [0.1, 0.2, 0.3]}
        result = retrieve_similar_nodes([0.1, 0.2, 0.3], small_dict, top_k=3)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], "node1")

if __name__ == "__main__":
    unittest.main()