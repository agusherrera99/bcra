FROM ubuntu:latest
MAINTAINER agustinherrera.dev@gmail.com

# Instalar cron
RUN apt-get update && \
    apt-get install -y git cron && \
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

RUN cat crons/*_cron > final_cron && crontab final_cron
RUN touch /var/log/ipc_interanual.log /var/log/ipc_mensual.log /var/log/tasa_depositos_30.log /var/log/tipo_cambio_minorista.log

CMD ["cron", "-f"]
