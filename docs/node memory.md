# Node Memory Overview

The Node Memory System stores all knowledge and context in the form of interconnected nodes. Each node represents a distinct unit of information, metadata, or control logic. Nodes can be linked together to form a memory graph that can be queried, traversed, and dynamically updated.


---

## Node Structure

Every node contains the following properties:

ID – A unique identifier (hash, UUID, or custom string).

Type – The node’s category (see below).

Content – The core data or meaning held by the node.

Tags – An optional list of semantic labels for classification.

Links – References to other related nodes (with optional relationship types).

Meta – Optional additional fields (timestamps, source, confidence, etc.).



---

## Node Types

1. data

Represents a concrete piece of information, such as a fact, event, concept, or memory. These form the bulk of the knowledge base.

> Example:
Type: data
Content: "Cats are often crepuscular animals."
Tags: [biology, animal_behavior]
Links: [#cat, #circadian]



2. tag

A node used as a semantic label or classification keyword. Tags help cluster and retrieve related nodes through shared labels.

> Example:
Type: tag
Content: psychology



3. control

Encodes structural or behavioral logic — such as priorities, constraints, triggers, rules, or memory policies.

> Example:
Type: control
Content: "Prune memory nodes older than 30 days with no links."
Tags: [decay_policy]




---

Example Node
```json
{
  "id": "n-21382",
  "type": "data",
  "content": "Lavi prefers to use dual swords.",
  "tags": ["character_trait", "combat"],
  "links": ["n-19873", "n-22113"],
  "meta": {
    "source": "user_input",
    "timestamp": "2025-04-13T18:24:00Z"
  }
}
```

---

Summary

By combining data, tag, and control nodes, the memory system becomes a flexible, interpretable graph of concepts and logic. This model supports advanced reasoning and context recall — especially useful in systems requiring long-term memory, adaptive behavior, or human-aligned knowledge processing.
