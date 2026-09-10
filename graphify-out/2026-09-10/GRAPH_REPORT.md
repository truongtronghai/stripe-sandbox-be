# Graph Report - stripe-sandbox-be  (2026-09-10)

## Corpus Check
- 13 files · ~2,366 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 42 nodes · 40 edges · 11 communities (5 shown, 2 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `67bb8c7c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- opencode.json
- graphify.js
- Guide for Agent
- main.py
- stripe-sandbox-be
- route.py
- stripe_webhook

## God Nodes (most connected - your core abstractions)
1. `Guide for Agent` - 6 edges
2. `stripe_webhook()` - 4 edges
3. `Item` - 3 edges
4. `update_item()` - 3 edges
5. `to_dict()` - 3 edges
6. `SuccessResponse` - 2 edges
7. `InProgressResponse` - 2 edges
8. `ErrorResponse` - 2 edges
9. `get_ws_route()` - 2 edges
10. `read_item()` - 2 edges

## Surprising Connections (you probably didn't know these)
- `stripe_webhook()` --calls--> `to_dict()`  [EXTRACTED]
  src/main.py → src/utils/converters/raw_bytes_literal.py

## Import Cycles
- None detected.

## Communities (11 total, 2 thin omitted)

### Community 0 - "opencode.json"
Cohesion: 0.50
Nodes (3): plugin, $schema, .opencode/plugins/graphify.js

### Community 2 - "Guide for Agent"
Cohesion: 0.29
Nodes (6): Commands, Development Policy, Gotchas, graphify, Guide for Agent, Project overview

### Community 4 - "main.py"
Cohesion: 0.32
Nodes (7): BaseModel, get, put, Item, read_item(), read_root(), update_item()

### Community 6 - "route.py"
Cohesion: 0.43
Nodes (6): FastAPI, ErrorResponse, get_ws_route(), InProgressResponse, SuccessResponse, TypedDict

### Community 9 - "stripe_webhook"
Cohesion: 0.40
Nodes (4): post, Request, stripe_webhook(), to_dict()

## Knowledge Gaps
- **8 isolated node(s):** `Project overview`, `Commands`, `Gotchas`, `graphify`, `Development Policy` (+3 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 22 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `stripe_webhook()` connect `stripe_webhook` to `main.py`?**
  _High betweenness centrality (0.043) - this node is a cross-community bridge._
- **What connects `Project overview`, `Commands`, `Gotchas` to the rest of the system?**
  _8 weakly-connected nodes found - possible documentation gaps or missing edges._