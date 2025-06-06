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
   - Tags are normalized using `normalize_tag()`:
     - Lowercased, stripped of whitespace/special characters.  
   - Duplicates are removed.  
   - A maximum of 5 valid tags is added per node (`MAX_TAGS` is configurable).

3. **Synonym Resolution** *(planned)*  
   - *[Currently unimplemented in code]*  
   - In the future, suggested tags will be compared against existing tags using:
     - Vector similarity (e.g. FAISS/Chroma)  
     - A predefined synonym dictionary  
   - Close matches may be normalized to an existing canonical tag.

4. **Tag Indexing & Logging**  
   - Tags are written into a persistent tag index (e.g. `tags.json`).  
   - Each tag maintains:
     - A list of associated node UUIDs  
     - Synonyms (future support)  
     - Creation timestamp and usage count (planned)  
   - A tagging event is also logged via `log_id_event()`.

---

## 🧠 Synonym Normalization

*(Not yet active – design stage)*

Synonym handling ensures that similar concepts are grouped under a single tag. This reduces fragmentation and improves retrieval quality.

**Planned approaches:**

- **Embedding similarity**  
  Each tag gets an embedding vector; new tags are compared via cosine similarity.

- **Manual/LLM-assisted curation**  
  A dictionary like:

  ```json
  {
    "memory": ["storage", "long-term", "brain", "retention"]
  }

If a tag like "brain" is submitted, it's mapped to "memory" if similarity is high enough (above a threshold, e.g. 0.8).


---

✅ Validation Rules

Max tags per node: 5 (MAX_TAGS)

Duplicate tags: removed automatically

Format: lowercase, alphanumeric, optional hyphen/underscore

Empty or invalid tags: discarded during normalization

Unknown tags: added automatically to the database with associated node UUIDs



---

🗂️ Tag Index Structure

A central tag index is used to track usage and perform normalization.

Current structure (tags.json):

{
  "memory": ["n-uuid1", "n-uuid2"],
  "context": ["n-uuid3"]
}

Future expansion:

{
  "memory": {
    "nodes": ["n-uuid1", "n-uuid2"],
    "synonyms": ["brain", "storage"],
    "created_at": "2025-06-04T12:33:00",
    "count": 22
  }
}


---

🔍 Tag Querying

Tags may later serve as filters in queries, e.g.:

Find all nodes tagged with:
- memory
- context

Planned support for fuzzy-matching queries like:

Find nodes similar to "retention" ➜ maps to "memory"


---

🛠️ Implementation Notes

The TagManager class is responsible for:

Loading and saving tag data (tags.json)

Validating and normalizing proposed tags

Preventing duplicates per node and globally

Logging tagging actions via log_id_event()


Tags are stored persistently across sessions.



---

💡 Future Ideas

Embedding-based tag synonym detection

Auto-deprecation of unused tags

Visualization of tag graph

LLM feedback loop to suggest merging tags

Human moderation of suspicious tags

