import json
import os

SYNONYM_FILE = os.path.join(os.path.dirname(__file__), 'synonyms.json')

def load_synonym_dict():
    if not os.path.exists(SYNONYM_FILE):
        return {}
    with open(SYNONYM_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

synonym_dict = load_synonym_dict()

# Odwrócenie słownika do lookupu odwrotnego: "brain" ➜ "memory"
reverse_lookup = {}
for canonical, synonyms in synonym_dict.items():
    reverse_lookup[canonical] = canonical
    for synonym in synonyms:
        reverse_lookup[synonym] = canonical

def normalize_tag(tag):
    tag = tag.strip().lower()
    return reverse_lookup.get(tag, tag)