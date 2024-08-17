DC = docker-compose
NGINX = docker_compose/nginx.yaml
STORAGES_FILE = docker_compose/postgres.yaml
STORAGES_FILE_COPY = docker_compose/backup.yaml
APP_FILE = docker_compose/app.yaml
MONITORING_FILE = docker_compose/monitoring.yaml
EXEC = docker exec -it
NGINX_CONTAINER = nginx
DB_CONTAINER = ppostgres
DB_CONTAINER_COPY = ppostgres_backup
LOGS = docker logs
ENV_FILE = --env-file .env
APP_CONTAINER = app-drf-shop
INTO_BASH_FOR_MIGRATE = /bin/bash -c
INTO_BASH = /bin/bash
ENTER_POSTGRES_CONTAINER = psql -U postgres -d drfshop
RUN_MIGRATION = poetry run python manage.py migrate
RUN_COLLECTSTATIC = poetry run python manage.py collectstatic --noinput
RUN_CREATESUPERUSER = poetry run python manage.py createsuperuser

.PHONY: monitoring
monitoring:
	${DC} -f ${MONITORING_FILE} ${ENV_FILE} up --build -d

.PHONY: monitoring-logs
monitoring-logs:
	${DC} -f ${MONITORING_FILE} ${ENV} logs -f

.PHONY: monitoring-down
monitoring-down:
	${DC} -f ${MONITORING_FILE} down

.PHONY: nginx
nginx:
	${DC} -f ${NGINX} up -d

.PHONY: nginx-logs
nginx-logs:
	${LOGS} ${NGINX_CONTAINER}

.PHONY: storages
storages:
	${DC} -f ${STORAGES_FILE} -f ${STORAGES_FILE_COPY} ${ENV_FILE} up -d

.PHONY: storages-down
storages-down:
	${DC} -f ${STORAGES_FILE} -f ${STORAGES_FILE_COPY} down

.PHONY: storages-logs
storages-logs:
	${LOGS} ${DB_CONTAINER} -f
 
.PHONY: app
app:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} -f ${STORAGES_FILE_COPY} ${ENV_FILE} up -d

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} down

.PHONY: migrate
migrate:
	${EXEC} ${APP_CONTAINER} ${INTO_BASH_FOR_MIGRATE} "${RUN_MIGRATION}"

.PHONY: collectstatic
collectstatic:
	${EXEC} ${APP_CONTAINER} ${INTO_BASH_FOR_MIGRATE} "${RUN_COLLECTSTATIC}"

.PHONY: createsuperuser
createsuperuser:
	${EXEC} ${APP_CONTAINER} ${INTO_BASH_FOR_MIGRATE} "${RUN_CREATESUPERUSER}"

.PHONY: appbash
appbash:
	${EXEC} ${APP_CONTAINER} ${INTO_BASH}

.PHONY: dbbash
dbbash:
	${EXEC} ${DB_CONTAINER} ${ENTER_POSTGRES_CONTAINER}

.PHONY: full_clean
full_clean:
	${DC} down -v --remove-orphans ${DB_CONTAINER} ${DB_CONTAINER_COPY}

.PHONY: runtest
runtest:
	${EXEC} ${APP_CONTAINER} pytest