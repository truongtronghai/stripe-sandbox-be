# Dockerfile Explanation

This document explains the `Dockerfile` for the `stripe-sandbox-be` FastAPI backend, with focus on the multi-stage build and the runtime stage (lines 12-18).

## Full Dockerfile

```dockerfile
FROM python:3.11-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:0.12.5 /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

FROM python:3.11-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH="/app:/app/src" \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv

COPY pyproject.toml ./
COPY src ./src

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Multi-stage build

A multi-stage build uses multiple `FROM` statements. Each stage is a self-contained image; the final stage (the last one) is what ships. This lets us do heavy work (installing dependencies) in a build stage and copy only the finished artifacts into a slim runtime image.

- **Stage 1 — `builder`:** installs project dependencies using `uv`.
- **Stage 2 — `runtime`:** the final image; copies in only the virtualenv and the source code.

Why? The dependencies include compilers and build tools that would bloat the image if left in. By installing in the builder stage and copying only the resulting `.venv`, the runtime image stays small and has a minimal attack surface.

## Lines 12-18 (runtime stage)

```dockerfile
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

COPY --from=builder /build/.venv /app/.venv
```

### `ENV` (lines 12-15)

Sets runtime environment variables for every subsequent command and for the running container:

- `PYTHONDONTWRITEBYTECODE=1` — stops Python from writing `.pyc` bytecode caches. Keeps the image clean and avoids writes to a read-only filesystem.
- `PYTHONUNBUFFERED=1` — forces Python's stdout/stderr to be line-buffered, so logs appear in Docker logs immediately instead of being held in a buffer (important for `docker logs`).
- `PYTHONPATH="/app:/app/src"` — makes both the repo root and the `src/` directory importable. Required because `src/main.py` mixes two import styles: `from src.ws_route...` (needs `/app` on the path) and `from utils...` (needs `/app/src` on the path, since `utils/` lives inside `src/`).
- `PATH="/app/.venv/bin:$PATH"` — prepends the app's virtualenv `bin` directory to the PATH, so the tools installed there (`uvicorn`, etc.) can be invoked by name without a full path.

### `WORKDIR /app` (line 17)

Sets the current working directory to `/app` for all following instructions (`COPY`, `CMD`). Every command now runs from this directory, and `uvicorn src.main:app` resolves module paths relative to it. Crucially, `src/` and `utils/` — imported by `src/main.py` — are accessible from here, so the app starts with the same layout as running it locally from the repo root.

### `COPY --from=builder /app/.venv /app/.venv` (line 19)

Copies the virtualenv that `uv sync` created in the builder stage (`/app/.venv`) into the runtime image at `/app/.venv`.

This is the heart of the multi-stage pattern, and it has an important constraint:

- `--from=builder` — the source is the `builder` stage, not the build context.
- Only the dependency installation result is transferred; build-time tooling stays behind.
- The venv must be created **at its final runtime path** (`/app/.venv`), matching the runtime `WORKDIR`. `uv` bakes the interpreter's absolute path into console-script shebangs (e.g. `bin/uvicorn` starts with `#!/app/.venv/bin/python`). Creating the venv at one path (`/build/.venv`) and copying it elsewhere breaks those shebangs — the container then fails to start with `exec /app/.venv/bin/uvicorn: no such file or directory`.

## Build & run

```bash
docker build -t stripe-sandbox-be .
docker run --rm -p 8000:8000 stripe-sandbox-be
```

Exposing the port:

- `EXPOSE 8000` — documents that the container listens on port 8000.
- `CMD` runs `uvicorn src.main:app --host 0.0.0.0 --port 8000`. Binding to `0.0.0.0` makes it reachable from outside the container.
- `docker run -p 8000:8000` publishes the container's port 8000 to the host, so `http://localhost:8000` (and the machine's network IP) reach the app.

## Notes

- `uv sync --frozen --no-dev --no-install-project` installs only production dependencies, pinned to `uv.lock`, without building the project package itself.
- `UV` is pinned to the same version (0.12.5) used locally for reproducible builds.
- A `.dockerignore` excludes `.venv`, `__pycache__`, `graphify-out/` etc., keeping the build context small.
- Two gotchas this Dockerfile avoids: (1) creating the venv at a path different from its runtime location breaks console-script shebangs; (2) the app's mixed imports (`src.ws_route` + flat `utils`) require both `/app` and `/app/src` on `PYTHONPATH`.