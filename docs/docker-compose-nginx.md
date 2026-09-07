# Docker Compose + Nginx — localhost setup

Simple localhost-only orchestration for the `stripe-sandbox-be` FastAPI backend: a minimal Nginx reverse proxy in front of the API.

## Architecture

```
Client ──> Nginx (host port 80) ──> api (FastAPI, port 8000, internal only)
                                    └── WebSocket /ws (upgraded by Nginx)
```

- **`api`** — built from the existing `Dockerfile`, listens on port 8000. Not published to the host; Nginx is the only entry point.
- **`nginx`** — minimal reverse proxy on host port 80. Proxies HTTP and WebSocket traffic to `api`.

## docker-compose.yaml

```yaml
services:
  api:
    build:
      context: .
      dockerfile: Dockerfile
    restart: unless-stopped
    expose:
      - "8000"
    networks:
      - backend

  nginx:
    image: nginx:1.27-alpine
    restart: unless-stopped
    ports:
      - "80:80"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - api
    networks:
      - backend

networks:
  backend:
    driver: bridge
```

## nginx.conf

- `proxy_pass http://api:8000` — resolves the `api` service by Compose network name.
- Forwarded headers (`Host`, `X-Real-IP`, `X-Forwarded-For`, `X-Forwarded-Proto`) so the backend sees the real client.
- `/ws` location adds `Upgrade` / `Connection: upgrade` headers plus 3600s timeouts so the FastAPI WebSocket endpoint works through Nginx.

## Run

```bash
docker compose up -d --build
docker compose ps
docker compose logs -f api nginx
docker compose down
```

Test:

```bash
curl http://localhost/
curl http://localhost/items/1
```

Notes:

- The API has no published port; to reach it directly for debugging use `docker compose exec api bash`.
- This setup is for localhost only. Add TLS and real certs when moving to production; the container already listens on 443 for Nginx to use later.