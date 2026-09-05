# Graph Report - stripe-sandbox-be  (2026-09-04)

## Corpus Check
- 8 files · ~600 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 19 nodes · 12 edges · 8 communities (3 shown, 2 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `fabb4e94`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- opencode.json
- graphify.js
- Guide for Agent
- get
- stripe-sandbox-be

## God Nodes (most connected - your core abstractions)
1. `Guide for Agent` - 3 edges
2. `plugin` - 2 edges
3. `read_root()` - 2 edges
4. `read_item()` - 2 edges
5. `$schema` - 1 edges
6. `.opencode/plugins/graphify.js` - 1 edges
7. `IMPORTANT: keep the reminder string free of backticks and $(...) constructs.` - 1 edges
8. `graphify` - 1 edges
9. `Development Policy` - 1 edges
10. `stripe-sandbox-be` - 0 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (8 total, 2 thin omitted)

### Community 0 - "opencode.json"
Cohesion: 0.50
Nodes (3): plugin, $schema, .opencode/plugins/graphify.js

### Community 2 - "Guide for Agent"
Cohesion: 0.50
Nodes (3): Development Policy, graphify, Guide for Agent

### Community 4 - "get"
Cohesion: 0.67
Nodes (3): get, read_item(), read_root()

## Knowledge Gaps
- **5 isolated node(s):** `$schema`, `.opencode/plugins/graphify.js`, `stripe-sandbox-be`, `graphify`, `Development Policy`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 11 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What connects `$schema`, `.opencode/plugins/graphify.js`, `stripe-sandbox-be` to the rest of the system?**
  _5 weakly-connected nodes found - possible documentation gaps or missing edges._