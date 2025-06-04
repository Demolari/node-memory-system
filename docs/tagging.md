# 🏷️ Tagging System – Concept and Design

## Overview

This document outlines how the tagging system operates within the Node Memory System. Tags serve as metadata to classify and retrieve nodes efficiently. A well-maintained tag structure allows for scalable semantic search and better contextual organization.

---

## 🔁 Tag Lifecycle

Each tag in the system follows a lifecycle from suggestion to storage:

1. **LLM Suggestion**  
   - A Language Model suggests `N` raw tags (e.g. 5–10) based on node content.
   - Tags may include synonyms or variants.

2. **Validation & Cleanup**  
   - Duplicates are removed.
   - Non-alphanumeric characters are sanitized (if needed).
   - Tags are truncated to a maximum (e.g., 5 final tags per node).

3. **Synonym Resolution**  
   - Suggested tags are compared against existing tags using:
     - Vector similarity (e.g. embeddings in FAISS/Chroma)
     - A predefined synonym dictionary (if available)
   - Close matches are normalized to an existing canonical tag.

4. **Logging**  
   - All final tags are written to `tags_log.json` or a similar file.
   - New tags are added to the index with metadata:
     - Creation date
     - Frequency
     - Known synonyms (if known)

---

## 🧠 Synonym Normalization

Synonym handling ensures that similar concepts are grouped under a single tag. This reduces fragmentation and improves retrieval quality.

Approaches:
- **Embedding similarity**:  
  Each tag gets an embedding vector; new tags are compared via cosine similarity.
- **Manual/LLM-assisted curation**:  
  A dictionary like:
  ```json
  {
    "memory": ["storage", "long-term", "brain", "retention"]
  }
  ```

If a tag like `"brain"` is submitted, it's mapped to `"memory"` if similarity is high enough (above a threshold, e.g. 0.8).

---

## ✅ Validation Rules

* **Max tags per node**: 5 (configurable)
* **Duplicate tags**: removed automatically
* **Format**: lowercase, no whitespace, alphanumeric or underscore/hyphen
* **Unknown tags**: added to log/index unless flagged for moderation

---

## 🗂️ Tag Index Structure

A central tag index is used to track usage and perform normalization.

Example (`tags_index.json`):

```json
{
  "memory": {
    "synonyms": ["storage", "brain"],
    "created_at": "2025-06-04T12:33:00",
    "count": 22
  },
  "context": {
    "synonyms": [],
    "created_at": "2025-06-03T11:01:00",
    "count": 9
  }
}
```

---

## 🔍 Tag Querying

Tags may later serve as filters in queries, e.g.:

```
Find all nodes tagged with:
- memory
- context
```

Or fuzzy-matched queries like:

```
Find nodes similar to "retention" ➜ maps to "memory"
```

---

## 💡 Future Ideas

* Tag suggestion during editing
* Auto-deprecation of unused tags
* Visualization of tag graph
* LLM feedback loop to suggest merging tags
