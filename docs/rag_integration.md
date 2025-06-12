# 🧠 RAG Integration with Node Memory System

## 🎯 Purpose

This document describes how the node-based memory system integrates with a Retrieval-Augmented Generation (RAG) layer. The goal is to combine the structured, user-readable node memory with the flexibility and retrieval power of vector-based semantic search.

---

## 🧩 Architecture Overview

User Query ↓ Embedding Generation (Query) ↓ Vector Search in Memory Embeddings (FAISS / Chroma) ↓ Retrieved Node IDs ↓ Node Content Assembly → RAG Prompt ↓ LLM Output

Components:
- **Node Manager** – handles creation, update, and tagging of memory nodes.
- **Embedding Engine** – converts node text and queries into vector representations.
- **Vector Store** – database for fast similarity search.
- **Retrieval Layer** – fetches and ranks relevant node content.
- **RAG Layer** – assembles context window and interacts with LLM.

---

## 🔁 Data Flow

### When a node is created or updated:
- Text is passed to an embedding model.
- Embedding is stored alongside node metadata in the vector store.

### When a query is made:
1. Convert query to embedding.
2. Search the vector store for top-k most similar nodes.
3. Retrieve matching node contents.
4. Assemble prompt using node content.
5. Feed prompt to LLM.

---

## 🔍 Retrieval Process

- Vector similarity search (e.g. cosine distance)
- Optional tag filtering or node scoring
- Retrieved nodes may be:
  - Directly passed to LLM
  - Summarized/condensed into a single paragraph

---

## 🛠 Embedding Storage

- Embeddings stored in `/memory/embeddings.json` or `.pkl`
- Mapping format: `{node_id: embedding_vector}`
- Embeddings regenerated on:
  - Node creation
  - Node edit (TBD)

---

## 🧶 Recontextualization

If multiple relevant nodes are returned:
- Chunk contents by priority
- Possibly summarize or compress for prompt size limits

If no node matches:
- Fallback to external knowledge or baseline LLM behavior
- Optionally use tag-based lookup

---

## 🚧 Limitations

- Embeddings not auto-updated after node edits (to do)
- No scoring based on recency or strength (to do)
- No cache mechanism yet

---

## 📌 Future Considerations

- Embedding version control (when using different models)
- Confidence scoring and weights
- Full-text search fallback
- User-customized RAG pipelines