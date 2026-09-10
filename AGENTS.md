# Guide for Agent

## Project overview

Small Python 3.11 **FastAPI** service that acts as a local Stripe sandbox for a companion
frontend. No database, no auth. All source lives under `src/`:

- Entrypoint: `src/main.py` -> `app` (declared in `pyproject.toml` under `[tool.fastapi]`)
- Routes: `POST /stripe-webhook` (src/main.py:34), scratch CRUD under `/items/*`, WebSocket `/ws` (src/ws_route/route.py)
- `src/utils/converters/raw_bytes_literal.py` holds `to_dict()`, the bytes->dict helper
  used by the webhook handler
- `src/stripe_sandbox_be/` is an empty `__init__.py` package; `sample.py` at repo root is
  a scratch file of Python tutorial examples, not part of the app
- Dev/docs detail lives in `docs/*.md` (Dockerfile and compose+nginx explainers); README is one line

## Commands

Everything goes through `uv` (pinned to 0.12.5, same as the Docker builder stage):

- Install deps: `uv sync`
- Run dev server: `uv run uvicorn src.main:app --reload` (or `uv run fastapi dev src/main.py`)
- Lint / format: `uv run ruff check .` and `uv run ruff format .`
- Pre-commit hooks (ruff-check + ruff-format): `uv run pre-commit run --all-files`
- Local stack (Nginx on host :80 -> unexposed api :8000): `docker compose up -d --build`

There is **no test suite** (no pytest dependency, no test files). Verification is ruff +
manual curl / websocket calls; add a test framework before writing tests.

## Gotchas

- **Mixed import styles are load-bearing — do not "unify" them.** `src/main.py` imports
  `from src.ws_route...` (repo-root-relative) _and_ flat `from utils.converters...`
  (src/-relative). These only work together because both repo root and `src/` are on the
  path: Docker sets `PYTHONPATH=/app:/app/src`, and locally `uv run` injects `src/`. Running
  bare `uvicorn`/`python` from a plain venv breaks the `utils.*` imports.
- Importable module folders cannot contain hyphens (comment at src/main.py:4).
- WebSocket `/ws` is reverse-proxied by Nginx with Upgrade headers and 3600s proxy timeouts
  (`nginx/nginx.conf`) — keep those; the API container itself is not published, debug via
  `docker compose exec api bash`.
- Dockerfile: the venv must be installed at its final runtime path (`/app/.venv`) or the
  uvicorn console-script shebang breaks (`docs/dockerfile-explanation.md` explains why).

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

When the user types `/graphify`, use the installed graphify skill or instructions before doing anything else.

Rules:

- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- Dirty graphify-out/ files are expected after hooks or incremental updates; dirty graph files are not a reason to skip graphify. Only skip graphify if the task is about stale or incorrect graph output, or the user explicitly says not to use it.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).

## Development Policy

Superpowers is installed and available.

Use Superpowers skills when they provide meaningful value, but use engineering judgment
about process overhead.

For simple, low-risk changes such as:

- renaming
- mechanical refactoring
- obvious configuration changes

do not invoke TDD.

For normal features:

- implement the feature
- run relevant tests
- fix failures
- verify the result

Use test-driven-development for:

- complex business logic
- complex state transitions
- authentication/authorization
- non-trivial data transformations
- complex hooks
- high-risk behavior
- regression bugs where a regression test is valuable

When a bug is discovered, prefer writing a regression test before fixing it.

Always perform appropriate verification before declaring the task complete.
