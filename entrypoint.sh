#!/bin/bash

# Ожидание доступности порта PostgreSQL
wait_for_port() {
    local host=$1
    local port=$2
    local timeout=30
    local start_time=$(date +%s)

    echo "Ожидание доступности порта $host:$port..."

    while ! nc -z "$host" "$port" >/dev/null 2>&1; do
        sleep 1
        local current_time=$(date +%s)
        local elapsed_time=$((current_time - start_time))

        echo "Пробуем подключиться к $host:$port..."

        if [ $elapsed_time -ge $timeout ]; then
            echo "Не удалось подключиться к $host:$port за $timeout секунд"
            exit 1
        fi
    done

    echo "Порт $host:$port доступен"
}

# Ожидание доступности PostgreSQL
wait_for_port "postgres" 5432

# Запуск Django-приложения (или другого приложения)
echo "Запуск приложения..."
exec poetry run python manage.py