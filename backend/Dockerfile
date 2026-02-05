FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN addgroup --system app && adduser --system --ingroup app app

WORKDIR /app

COPY --chown=app:app requirements.txt /app/
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY --chown=app:app . /app/

ENV DJANGO_SETTINGS_MODULE=config.settings.prod \
    DEBUG=0 \
    SECRET_KEY=unsafe-build-secret \
    ALLOWED_HOSTS=localhost,127.0.0.1

RUN python manage.py collectstatic --noinput

USER app

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]