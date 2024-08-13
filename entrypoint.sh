#!/bin/bash

# Ожидание доступности порта PostgreSQL
# wait_for_port() {
#     local host=$1
#     local port=$2
#     local timeout=30
#     local start_time=$(date +%s)

#     echo "Waiting for port $host:$port to be available..."

#     while ! nc -z "$host" "$port" >/dev/null 2>&1; do
#         sleep 1
#         local current_time=$(date +%s)
#         local elapsed_time=$((current_time - start_time))

#         echo "Trying to connect to $host:$port..."

#         if [ $elapsed_time -ge $timeout ]; then
#             echo "Failed to connect to $host:$port within $timeout seconds"
#             exit 1
#         fi
#     done

#     echo "Port $host:$port is available"
# }

# Ожидание доступности PostgreSQL
# wait_for_port "postgres" 5432

# Запуск Django-приложения (или другого приложения)
echo "Запуск приложения..."
exec poetry run gunicorn core.project.wsgi:application --workers 4 --bind 0.0.0.0:8000