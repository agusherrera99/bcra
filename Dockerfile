FROM python:3.12-slim-trixie

# Instalar cron
RUN apt-get update && \
    apt-get install -y git && \
    apt-get install -y cron && \
    rm -rf /var/lib/apt/lists/*

# Instalar UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
COPY . .

# Deshabilitar dependencias de desarrollo
ENV UV_NO_DEV=1
# Sincronizar el proyecto en un nuevo ambiente, asegurando que el lockfile este actualizado.
RUN uv add git+https://github.com/agusherrera99/google_sheet_util.git@main
RUN uv sync --locked


COPY ./bcra_cronjob /etc/cron.d/bcra_cronjob
RUN chmod 0644 /etc/cron.d/bcra_cronjob

CMD ["cron", "-f"]
