# Graph Report - stripe-sandbox-be  (2026-09-06)

## Corpus Check
- 8 files · ~855 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 26 nodes · 20 edges · 9 communities (4 shown, 2 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c26edbe9`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- opencode.json
- graphify.js
- Guide for Agent
- get
- stripe-sandbox-be
- Item

## God Nodes (most connected - your core abstractions)
1. `Guide for Agent` - 3 edges
2. `Item` - 3 edges
3. `update_item()` - 3 edges
4. `read_root()` - 2 edges
5. `read_item()` - 2 edges
6. `plugin` - 2 edges
7. `graphify` - 1 edges
8. `Development Policy` - 1 edges
9. `$schema` - 1 edges
10. `.opencode/plugins/graphify.js` - 1 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (9 total, 2 thin omitted)

### Community 0 - "opencode.json"
Cohesion: 0.50
Nodes (3): plugin, $schema, .opencode/plugins/graphify.js

### Community 2 - "Guide for Agent"
Cohesion: 0.50
Nodes (3): Development Policy, graphify, Guide for Agent

### Community 4 - "get"
Cohesion: 0.67
Nodes (3): get, read_item(), read_root()

### Community 6 - "Item"
Cohesion: 0.50
Nodes (4): BaseModel, put, Item, update_item()

## Knowledge Gaps
- **5 isolated node(s):** `graphify`, `Development Policy`, `stripe-sandbox-be`, `$schema`, `.opencode/plugins/graphify.js`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 15 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Item` connect `Item` to `get`?**
  _High betweenness centrality (0.020) - this node is a cross-community bridge._
- **Why does `update_item()` connect `Item` to `get`?**
  _High betweenness centrality (0.020) - this node is a cross-community bridge._
- **What connects `graphify`, `Development Policy`, `stripe-sandbox-be` to the rest of the system?**
  _5 weakly-connected nodes found - possible documentation gaps or missing edges._