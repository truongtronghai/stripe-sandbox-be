# Graph Report - stripe-sandbox-be  (2026-09-10)

## Corpus Check
- 16 files · ~2,580 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 48 nodes · 49 edges · 12 communities (5 shown, 2 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `933e1c3b`
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
2. `get_dynamodb()` - 4 edges
3. `get_ws_route()` - 4 edges
4. `stripe_webhook()` - 4 edges
5. `ensure_subscription_table()` - 3 edges
6. `Item` - 3 edges
7. `update_item()` - 3 edges
8. `to_dict()` - 3 edges
9. `SuccessResponse` - 2 edges
10. `InProgressResponse` - 2 edges

## Surprising Connections (you probably didn't know these)
- `get_ws_route()` --calls--> `get_dynamodb()`  [EXTRACTED]
  src/ws_route/route.py → src/db/get_db.py
- `get_ws_route()` --calls--> `ensure_subscription_table()`  [EXTRACTED]
  src/ws_route/route.py → src/db/subscription_table.py
- `stripe_webhook()` --calls--> `to_dict()`  [EXTRACTED]
  src/main.py → src/utils/converters/raw_bytes_literal.py

## Import Cycles
- None detected.

## Communities (12 total, 2 thin omitted)

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
Cohesion: 0.27
Nodes (9): FastAPI, get_dynamodb(), Get the DynamoDB resource pointing to Floci., ensure_subscription_table(), ErrorResponse, get_ws_route(), InProgressResponse, SuccessResponse (+1 more)

### Community 9 - "stripe_webhook"
Cohesion: 0.40
Nodes (4): post, Request, stripe_webhook(), to_dict()

## Knowledge Gaps
- **8 isolated node(s):** `stripe-sandbox-be`, `$schema`, `.opencode/plugins/graphify.js`, `Commands`, `Development Policy` (+3 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 24 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `stripe_webhook()` connect `stripe_webhook` to `main.py`?**
  _High betweenness centrality (0.042) - this node is a cross-community bridge._
- **What connects `stripe-sandbox-be`, `$schema`, `.opencode/plugins/graphify.js` to the rest of the system?**
  _8 weakly-connected nodes found - possible documentation gaps or missing edges._