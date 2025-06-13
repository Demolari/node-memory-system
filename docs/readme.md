# Node Memory System

**Status**: Conceptual phase  
**Type**: Documentation & Design  
**Author**: [Demolari](https://github.com/Demolari)

---

## 📌 Overview

The **Node Memory System** is an experimental idea for building a long-term memory structure for large language models (LLMs).  
Instead of storing plain text or embeddings in isolation, the system organizes information in a **graph of nodes**, where each node represents a specific memory unit, tag, or control structure.

This graph-based memory is designed to enhance retrieval, relevance, and the ability to track long-term context over time — potentially hybridizing with techniques like **RAG** (Retrieval-Augmented Generation).

---

## 🧠 Core Concepts

### Node Types

- **Data Node**  
  Stores knowledge, facts, experiences, or contextual information.

- **Tag Node**  
  Represents concepts, topics, people, locations, timelines, etc.  
  Used to categorize or cluster related Data Nodes.

- **Control Node**  
  Meta-level structure for navigation, querying, or managing memory flow.  
  For example: conversation logs, session grouping, timeline branches.

### Relationships

Nodes are connected using **graph-like edges** which define the nature of their relation:
- Similarity
- Causality
- Tagging
- Temporal links
- Contextual dependency

This allows flexible traversal of memory depending on query goals.

---

## 📂 Project Structure

- [`docs/README.md`](docs/README.md) – This file
- [`docs/nodes.md`](docs/nodes.md) – Description of node types, structure, and metadata
- [`docs/architecture.md`](docs/architecture.md) – Internal structure of the system and graph layout

> ✅ Additional docs will be added as the project evolves.

---

## 🚫 No Executable Code Yet

This repository currently contains **design documentation only**.  
There are **no runnable files or Python scripts**, and no installation steps required.

If you’re here for code, you’re early — but welcome! Feel free to follow or contribute ideas.

---

## 📝 License

This project **does not currently have a license**.  
That means all rights are reserved to the author.

If you'd like to use or adapt part of this work, please open an issue or contact me directly.

---

## Requirements

Make sure to install all needed libraries
```bash
pip install -r requirements.txt
```
---

## 🙋 Contact

Feel free to create an issue with ideas, questions, or suggestions.  
You can also reach out via GitHub: [Demolari](https://github.com/Demolari)
