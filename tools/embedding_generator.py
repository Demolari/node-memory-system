import os
import json
import pickle
from sentence_transformers import SentenceTransformer

class EmbeddingGenerator:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def generate_embeddings(self, data):
        texts = [item["text"] for item in data]
        embeddings = self.model.encode(texts, show_progress_bar=True)
        return embeddings

    def save_embeddings(self, embeddings, path="embeddings/embeddings.pkl"):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            pickle.dump(embeddings, f)

    def load_node_data(self, path="memory/nodes.json"):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def generate_and_save(self):
        data = self.load_node_data()
        embeddings = self.generate_embeddings(data)
        self.save_embeddings(embeddings)
        print(f"✅ Embeddings generated and saved for {len(data)} nodes.")


if __name__ == "__main__":
    generator = EmbeddingGenerator()
    generator.generate_and_save()