# syntax=docker/dockerfile:1.7
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev && rm -rf /var/lib/apt/lists/*

ENV PIP_DEFAULT_TIMEOUT=100

COPY requirements.txt .

# --mount=type=cache persists pip's download cache across builds (via
# BuildKit), so a retry after a network blip resumes from what's already
# downloaded instead of starting over. --retries/--timeout give pip its
# own resilience against slow/flaky connections.
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --retries 10 --timeout 100 -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
