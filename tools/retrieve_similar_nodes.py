import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Ścieżka do pliku z embeddingami
EMBEDDING_FILE = "embeddings/embeddings.pkl"

# Model do generowania embeddingów (taki sam jak używany wcześniej!)
MODEL_NAME = "all-MiniLM-L6-v2"

# Liczba wyników do zwrócenia
TOP_K = 4


def load_embeddings(filepath=EMBEDDING_FILE):
    with open(filepath, "rb") as f:
        return pickle.load(f)


def generate_query_embedding(text, model):
    return model.encode([text])


def retrieve_similar_nodes(query, top_k=TOP_K):
    # Wczytaj dane
    embeddings = load_embeddings()
    node_ids = list(embeddings.keys())
    vectors = np.array(list(embeddings.values()))

    # Wygeneruj embedding zapytania
    model = SentenceTransformer(MODEL_NAME)
    query_vector = generate_query_embedding(query, model)

    # Oblicz podobieństwo kosinusowe
    similarities = cosine_similarity(query_vector, vectors)[0]
    top_indices = similarities.argsort()[::-1][:top_k]

    # Zwróć dopasowane node_id i podobieństwo
    return [
        (node_ids[i], float(similarities[i])) for i in top_indices
    ]


if __name__ == "__main__":
    user_query = input("🔍 Enter your query:\n> ")
    results = retrieve_similar_nodes(user_query)

    print("\n📌 Top matching nodes:")
    for node_id, score in results:
        print(f"  - {node_id} (score: {score:.4f})")