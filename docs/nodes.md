# Node Memory System: Node Structure and Behavior

## Overview
A high-level explanation of what a "node" is in the context of this memory system.  
(Ex. A node is a container for a memory fragment, concept, or unit of information...)

## Node Types
- **Memory nodes** – store episodic or factual memory
- **Tag nodes** – link to concepts, emotions, or categories
- **System nodes** – used for structural/meta data

## Node Structure
What are the essential components of a node?
- ID or unique identifier
- Timestamp / creation date
- Data payload (text, embeddings, etc.)
- Links to other nodes (inbound / outbound)
- Tags or metadata

## Link Behavior
How nodes are connected to each other:
- Directed vs bidirectional links
- Link weight or priority (if used)
- Example: Memory node ↔ Concept tag

## Storage Format
Explain how a node might be stored on disk:
- Human-readable text (e.g., JSON, Markdown)
- Embedding vector storage (if used)
- File naming convention (e.g., node_0001.json)

## Access and Retrieval
- How nodes are found
- How link traversal works
- Simple search vs RAG-assisted lookup

## Editing and Mutation
- Can nodes be edited after creation?
- Versioning or historical snapshots
- Node “aging” or decay if you implement that

## Example Node (Markdown or JSON snippet)
```json
{
  "id": "node_0001",
  "type": "memory",
  "created": "2025-05-27T12:00:00Z",
  "data": "I had an idea about node linking while walking.",
  "tags": ["idea", "nodes", "walk"],
  "links": ["node_0002", "tag_idea_generation"]
}
```

---

Future Extensions

(placeholder for later):

Node compression?

Visualization tools?

Import/export?

---

# Node Graph Test Model
```json
{
  "nodes": [
    {
      "id": "n1",
      "type": "memory",
      "title": "Concept: Node-Based Memory",
      "content": "Idea for a memory system using connected nodes with relationships.",
      "tags": ["architecture", "memory"]
    },
    {
      "id": "n2",
      "type": "tag",
      "title": "architecture"
    },
    {
      "id": "n3",
      "type": "tag",
      "title": "memory"
    },
    {
      "id": "n4",
      "type": "system",
      "title": "RAG Integration",
      "content": "Use Retrieval-Augmented Generation for node access and expansion."
    },
    {
      "id": "n5",
      "type": "memory",
      "title": "Memory Token Cost Concern",
      "content": "Idea about exporting chat to reduce token consumption."
    }
  ],
  "edges": [
    { "from": "n1", "to": "n2", "type": "has_tag" },
    { "from": "n1", "to": "n3", "type": "has_tag" },
    { "from": "n1", "to": "n4", "type": "related" },
    { "from": "n1", "to": "n5", "type": "expanded_by" }
  ]
}
```