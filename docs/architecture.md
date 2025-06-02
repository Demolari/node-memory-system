# Architecture

This document outlines the high-level architecture of the Node Memory System. It describes the main components, their responsibilities, and the relationships between them.

## Purpose

The goal of the architecture is to provide a flexible and modular foundation for a memory system that can enhance or augment large language models with persistent, graph-based memory. This is a conceptual specification; no implementation is required at this stage.

---

## Core Components

### 1. Node Graph
A persistent structure that stores information in the form of interconnected nodes.

- Nodes contain data (content, metadata, references).
- Edges represent relationships, enabling memory traversal and context generation.

Types of nodes:
- **Data** – factual or contextual information (e.g. "Lavi is a character", "Kotori are humanoid cats").
- **Tag** – classifiers used to organize or retrieve nodes (e.g. "character", "race").
- **Control** – system-level nodes (e.g. recent queries, instructions, prompts).

---

### 2. Retrieval Layer
Responsible for selecting relevant nodes based on a query or prompt.

- Uses similarity search, tags, or structural traversal.
- May be augmented with vector embeddings or heuristics.
- Outputs a context set for generation.

---

### 3. Insertion/Update Layer
Handles the creation and mutation of nodes.

- Adds new data after generation or user input.
- Links new nodes to related existing ones.
- Maintains node uniqueness (via hashes or fuzzy matching).

---

### 4. Interaction Layer
The interface between the system and the language model (or human).

- Provides hooks to insert, retrieve, and query the graph.
- Can be implemented via plugins, scripts, or API calls.

---

## Data Flow (Example)

1. A user prompt is sent to the LLM:  
   _"Who is Abigail?"_

2. The **retrieval layer** finds relevant nodes:
   - Abigail (Data)
   - Kotori (Tag)
   - Lavi (linked context)

3. The retrieved nodes are passed as **augmented context** to the LLM.

4. The model generates a response:  
   _"Abigail is a young kotori who lives with an elven herbalist..."_

5. The **insertion layer** updates the graph with new facts, if needed.

---

## Flexibility

- The system is **model-agnostic**.
- Can be applied in different use cases:
  - Personal assistants
  - Narrative worldbuilding
  - Research agents

---

## Future Features (Optional)

- Versioning of nodes
- Forgetting / decay mechanisms
- Interactive graph visualization
- Long-term goal planning modules

---

## Summary

This architecture provides a high-level conceptual overview of how a node-based memory system can be structured. Each layer can be extended, swapped, or simulated independently.