import os
import pickle
from sentence_transformers import SentenceTransformer, util

EMBEDDINGS_PATH = "embeddings/embeddings.pkl"
MODEL_NAME = "all-MiniLM-L6-v2"

# Inicjalizacja modelu
model = SentenceTransformer(MODEL_NAME)

def load_embeddings():
    if not os.path.exists(EMBEDDINGS_PATH):
        raise FileNotFoundError(f"Nie znaleziono pliku {EMBEDDINGS_PATH}. Upewnij się, że embeddingi zostały wygenerowane.")
    with open(EMBEDDINGS_PATH, "rb") as f:
        return pickle.load(f)  # Format: list[dict] z kluczami: id, text, embedding

def retrieve_similar_nodes(query, top_k=4):
    data = load_embeddings()
    query_embedding = model.encode(query, convert_to_tensor=True)

    # Oblicz podobieństwo kosinusowe
    similarities = [
        {
            "id": item["id"],
            "text": item["text"],
            "score": float(util.cos_sim(query_embedding, item["embedding"])[0])
        }
        for item in data
    ]

    # Sortuj malejąco wg podobieństwa i zwróć top_k
    return sorted(similarities, key=lambda x: x["score"], reverse=True)[:top_k]

if __name__ == "__main__":
    user_input = input("🔎 Co chcesz wyszukać w pamięci?\n> ")
    results = retrieve_similar_nodes(user_input)
    print("\n📌 Najbardziej podobne węzły:")
    for res in results:
        print(f"\n🧠 ID: {res['id']}\n📝 Tekst: {res['text']}\n📈 Dopasowanie: {res['score']:.4f}")