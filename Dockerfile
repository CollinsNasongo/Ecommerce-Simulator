# ────────────────
# 1) Build Stage
# ────────────────
FROM python:3.11-slim-bookworm AS build

WORKDIR /app

# 1a) Re-write sources.list to point explicitly at Bookworm
RUN printf "deb http://deb.debian.org/debian bookworm main contrib non-free\n"    > /etc/apt/sources.list \
 && printf "deb http://deb.debian.org/debian bookworm-updates main contrib non-free\n" >> /etc/apt/sources.list \
 && printf "deb http://security.debian.org/debian-security bookworm-security main contrib non-free\n" >> /etc/apt/sources.list

# 1b) Install build-time deps
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      gcc \
      libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# 1c) Pre-build wheels for your Python dependencies
COPY requirements.txt .
RUN pip wheel --wheel-dir=/wheels -r requirements.txt

# 1d) Copy source & install from wheels
COPY . .
RUN pip install --no-index --find-links=/wheels -r requirements.txt


# ────────────────
#  2) Runtime Stage
# ────────────────
FROM python:3.11-slim-bookworm AS runtime

WORKDIR /app

# Bring in the Python runtime & libs from the build stage
COPY --from=build /usr/local/lib/python3.11 /usr/local/lib/python3.11

# Copy your application code
COPY --from=build /app /app

# Ensure your entrypoint can run
RUN chmod +x /app/entrypoint.sh

# Expose the Flask port
EXPOSE 5000

# Use your existing startup script
ENTRYPOINT ["bash", "/app/entrypoint.sh"]
