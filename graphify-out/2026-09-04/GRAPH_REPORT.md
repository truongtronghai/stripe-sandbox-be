# Graph Report - stripe-sandbox-be  (2026-09-04)

## Corpus Check
- 4 files · ~376 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 10 nodes · 6 edges · 4 communities (1 shown, 2 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d1721947`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- opencode.json
- graphify.js
- AGENTS.md

## God Nodes (most connected - your core abstractions)
1. `plugin` - 2 edges
2. `$schema` - 1 edges
3. `.opencode/plugins/graphify.js` - 1 edges
4. `IMPORTANT: keep the reminder string free of backticks and $(...) constructs.` - 1 edges
5. `graphify` - 1 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (4 total, 2 thin omitted)

### Community 0 - "opencode.json"
Cohesion: 0.50
Nodes (3): plugin, $schema, .opencode/plugins/graphify.js

## Knowledge Gaps
- **3 isolated node(s):** `$schema`, `.opencode/plugins/graphify.js`, `graphify`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 7 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What connects `$schema`, `.opencode/plugins/graphify.js`, `graphify` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._