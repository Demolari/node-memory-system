# Node Memory System – Detailed Documentation

This document provides a deeper technical overview of the **Node Memory System** for LLMs (Large Language Models), compared to the main `README.md`.

---

## 📌 Data Structure

The system is built around **nodes** (memory units) connected via directed relations. Each node can include:

- `id`: unique identifier
- `tags`: thematic keywords
- `content`: main content (text, thoughts, data)
- `links`: connections to other nodes (`id`, `relation`, `confidence`, etc.)
- `meta`: additional info (timestamp, source, model, etc.)

### Example Node (JSON):

```json
{
  "id": "node-001",
  "tags": ["RAG", "LLM", "memory"],
  "content": "Nodes can be used to map the thoughts of LLMs over a long timeline.",
  "links": [
    {
      "target": "node-002",
      "relation": "inspired_by",
      "confidence": 0.75
    }
  ],
  "meta": {
    "created": "2025-05-28T12:00:00Z",
    "model": "GPT-4.5",
    "source": "chat",
    "notes": "Important concept, needs follow-up"
  }
}


📂 Planned Documentation Folders

Folder	Description

docs/	Main project documentation
memory/	Example memory snapshots (JSON)
examples/	Usage examples, test scenarios, demos
tools/	Helper tools/scripts for memory management
spec/	Formal data format and API specifications



---

🔧 Development Notes / To-Do

[ ] Node search and retrieval strategy (embeddings + RAG?)

[ ] Tagging system and importance weighting

[ ] Integration with external sources (chat, files, APIs)

[ ] Memory versioning system

[ ] Node compression / merge strategy

[ ] Fact vs. hallucination marking

[ ] Reference implementation (Python / JavaScript?)



---

Note: This document will evolve as the project progresses.