# Graph Report - stripe-sandbox-be  (2026-09-11)

## Corpus Check
- 18 files · ~2,849 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 52 nodes · 48 edges · 16 communities (5 shown, 4 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `aa053212`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- opencode.json
- graphify.js
- Guide for Agent
- main.py
- stripe-sandbox-be
- ws_route/route.py
- webhook_route/route.py
- post
- Request

## God Nodes (most connected - your core abstractions)
1. `Guide for Agent` - 6 edges
2. `Item` - 3 edges
3. `update_item()` - 3 edges
4. `get_webhook_route()` - 3 edges
5. `get_ws_route()` - 3 edges
6. `read_root()` - 2 edges
7. `read_item()` - 2 edges
8. `SuccessResponse` - 2 edges
9. `InProgressResponse` - 2 edges
10. `ErrorResponse` - 2 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (16 total, 4 thin omitted)

### Community 0 - "opencode.json"
Cohesion: 0.50
Nodes (3): plugin, $schema, .opencode/plugins/graphify.js

### Community 2 - "Guide for Agent"
Cohesion: 0.29
Nodes (6): Commands, Development Policy, Gotchas, graphify, Guide for Agent, Project overview

### Community 4 - "main.py"
Cohesion: 0.28
Nodes (8): BaseModel, FastAPI, get, put, Item, read_item(), read_root(), update_item()

### Community 6 - "ws_route/route.py"
Cohesion: 0.43
Nodes (6): ErrorResponse, get_ws_route(), InProgressResponse, FastAPI, SuccessResponse, TypedDict

### Community 12 - "webhook_route/route.py"
Cohesion: 0.29
Nodes (4): get_dynamodb(), Get the DynamoDB resource pointing to Floci., get_webhook_route(), FastAPI

## Knowledge Gaps
- **8 isolated node(s):** `$schema`, `.opencode/plugins/graphify.js`, `Commands`, `Development Policy`, `Gotchas` (+3 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 28 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What connects `$schema`, `.opencode/plugins/graphify.js`, `Commands` to the rest of the system?**
  _8 weakly-connected nodes found - possible documentation gaps or missing edges._