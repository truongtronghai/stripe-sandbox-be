# Graph Report - stripe-sandbox-be  (2026-09-06)

## Corpus Check
- 9 files · ~961 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 29 nodes · 26 edges · 9 communities (4 shown, 2 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c77beebe`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- opencode.json
- graphify.js
- Guide for Agent
- main.py
- stripe-sandbox-be
- Item

## God Nodes (most connected - your core abstractions)
1. `Item` - 3 edges
2. `update_item()` - 3 edges
3. `get_ws_route()` - 3 edges
4. `Guide for Agent` - 3 edges
5. `read_root()` - 2 edges
6. `read_item()` - 2 edges
7. `plugin` - 2 edges
8. `$schema` - 1 edges
9. `.opencode/plugins/graphify.js` - 1 edges
10. `IMPORTANT: keep the reminder string free of backticks and $(...) constructs.` - 1 edges

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

### Community 4 - "main.py"
Cohesion: 0.48
Nodes (5): FastAPI, get, read_item(), read_root(), get_ws_route()

### Community 6 - "Item"
Cohesion: 0.50
Nodes (4): BaseModel, put, Item, update_item()

## Knowledge Gaps
- **5 isolated node(s):** `$schema`, `.opencode/plugins/graphify.js`, `Development Policy`, `graphify`, `stripe-sandbox-be`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 15 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Item` connect `Item` to `main.py`?**
  _High betweenness centrality (0.024) - this node is a cross-community bridge._
- **Why does `update_item()` connect `Item` to `main.py`?**
  _High betweenness centrality (0.024) - this node is a cross-community bridge._
- **What connects `$schema`, `.opencode/plugins/graphify.js`, `Development Policy` to the rest of the system?**
  _5 weakly-connected nodes found - possible documentation gaps or missing edges._