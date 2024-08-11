FROM python:3.12.1-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Обновление пакетов и установка зависимостей
RUN apt-get update -y && \
    apt-get install -y python3-dev \
                       gcc \
                       musl-dev \
                       libpq-dev \
                       nmap \
                       netcat

ADD pyproject.toml /app

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

COPY /src/* /app/
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]