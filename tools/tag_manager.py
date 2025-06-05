import os
import json
import re

# Maksymalna liczba tagów na node
MAX_TAGS = 5

# Ścieżki do plików
BASE_DIR = os.path.dirname(__file__)
TAG_DB_FILE = os.path.join(BASE_DIR, "tag_database.json")
SYNONYM_FILE = os.path.join(BASE_DIR, "synonyms.json")

# Wczytaj bazę synonimów
try:
    with open(SYNONYM_FILE, "r", encoding="utf-8") as f:
        synonym_dict = json.load(f)
except FileNotFoundError:
    synonym_dict = {}

# Wczytaj bazę tagów
try:
    with open(TAG_DB_FILE, "r", encoding="utf-8") as f:
        tag_db = set(json.load(f))
except FileNotFoundError:
    tag_db = set()


def normalize_tag(tag):
    """Zwraca znormalizowaną wersję tagu (bazując na bazie synonimów)"""
    tag = tag.lower().strip()
    for canonical, synonyms in synonym_dict.items():
        if tag == canonical or tag in synonyms:
            return canonical
    return tag


def is_valid_tag(tag):
    """Waliduje tag: musi być jednym słowem, bez znaków specjalnych"""
    return re.match(r"^[a-z0-9_]+$", tag) is not None


def process_tags(input_tags):
    """Oczyszcza, normalizuje, filtruje i ogranicza liczbę tagów"""
    clean_tags = []
    seen = set()

    for tag in input_tags:
        norm = normalize_tag(tag)
        if is_valid_tag(norm) and norm not in seen:
            clean_tags.append(norm)
            seen.add(norm)
        if len(clean_tags) >= MAX_TAGS:
            break

    return clean_tags


def add_tags_to_db(tags):
    """Dodaje tagi do lokalnej bazy i zapisuje ją"""
    new_tags = set(tags) - tag_db
    if new_tags:
        tag_db.update(new_tags)
        with open(TAG_DB_FILE, "w", encoding="utf-8") as f:
            json.dump(sorted(tag_db), f, indent=2)


# Przykładowe użycie
if __name__ == "__main__":
    raw_tags = ["AI", "machinelearning", "Brain", "storage", "weird@tag", "user"]
    final_tags = process_tags(raw_tags)
    add_tags_to_db(final_tags)

    print("Przetworzone tagi:", final_tags)
