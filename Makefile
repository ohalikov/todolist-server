rm:
	docker compose stop \
	&& docker compose rm \
	# && sudo rm -rf db_postgres/

up:
	docker compose build \
	&& docker compose -f docker-compose.yml up --force-recreate -d