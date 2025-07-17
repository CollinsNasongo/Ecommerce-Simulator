#!/usr/bin/env bash
set -e

# 1️⃣ Wait for Postgres
until pg_isready -h db -U "${DB_USER}"; do
  echo "⏳ Waiting for Postgres…"
  sleep 1
done

# 2️⃣ Seed initial SQL (runs only once)
psql -h db -U "$DB_USER" -d "$DB_NAME" -f /app/db/init.sql || true

# 3️⃣ Apply Alembic migrations
flask db upgrade

# 4️⃣ Launch Flask
exec flask run --host=0.0.0.0
