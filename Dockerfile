FROM python:3.12.1-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /shop

# Обновление пакетов и установка зависимостей
RUN apt-get update -y && \
    apt-get install -y python3-dev \
                       gcc \
                       musl-dev \
                       libpq-dev \
                       nmap \
                       netcat

COPY pyproject.toml /shop/
COPY manage.py /shop/

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

COPY /core/* /shop/
COPY entrypoint.sh /entrypoint.sh

RUN rm -rf *.pyc *.md \
    .idea/ docker_compose/ \
    __pycache__/ \
    core/project/settings/local_example.py \
    .git/ .pre-commit-config.yaml \
    .vscode/

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]