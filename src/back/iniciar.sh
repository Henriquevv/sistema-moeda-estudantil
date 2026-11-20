#!/bin/sh
# Prepara o banco e sobe a API; usado pelo contêiner na Render e no Docker.
set -e
alembic upgrade head
python -m app.tarefas.seed
exec uvicorn app.main:app --host 0.0.0.0 --port "${PORT:-8000}"
