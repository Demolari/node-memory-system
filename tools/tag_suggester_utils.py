import re

KEYWORDS = {
    "memory": ["storage", "brain", "retention"],
    "context": ["surroundings", "situation", "environment"],
    "system": ["architecture", "structure", "mechanism"],
    "AI": ["machine", "intelligence", "neural"],
}

def normalize_tag(tag):
    tag = tag.lower()
    tag = re.sub(r"[^a-z0-9_\-]", "", tag)
    return tag.strip()

def suggest_tags(text):
    suggestions = set()
    for base_tag, synonyms in KEYWORDS.items():
        for word in synonyms + [base_tag]:
            if word in text.lower():
                suggestions.add(base_tag)
                break
    return list(suggestions)