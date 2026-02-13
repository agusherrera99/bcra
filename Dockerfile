FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS builder

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv lock --upgrade-package google-sheet-util && \
    uv sync --frozen

FROM python:3.13-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    cron \
    git \
    ca-certificates \
    vim \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

COPY . .

RUN cat crons/*_cron > /etc/cron.d/bcra-cron && \
    chmod 0644 /etc/cron.d/bcra-cron && \
    crontab /etc/cron.d/bcra-cron

RUN touch /var/log/cron.log

CMD ["cron", "-f"]
