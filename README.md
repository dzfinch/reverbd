# Django + DRF + Postgres Starter

Production-ready starter infrastructure for a Django + Django REST Framework app with PostgreSQL, Docker, and CI.

## Quickstart (Docker)
1) Copy env file and tweak if needed:
   ```
   cp .env.example .env
   ```
2) Build and run:
   ```
   docker compose up --build
   ```
3) Visit: http://localhost:8000/healthz

## Migrations
```bash
docker compose run --rm web python manage.py migrate
```

## Create superuser
```bash
docker compose run --rm web python manage.py createsuperuser
```

## Local development notes
- The dev container runs Django `runserver` for auto-reload.
- `DATABASE_URL` defaults to the Postgres service in `docker-compose.yml`.
- Use `DJANGO_SETTINGS_MODULE=config.settings.dev` for local dev.

## Testing
```bash
docker compose run --rm web python manage.py test
```

## Deployment notes
- For early-stage deployment, Render or Railway are quick to set up.
- For later scale, migrate the same container to AWS (ECS/Fargate or EKS).
- Ensure `SECRET_KEY`, `DATABASE_URL`, and `ALLOWED_HOSTS` are set in production.

## Health check
`GET /healthz` returns:
```json
{"status": "ok"}
```