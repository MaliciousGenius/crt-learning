.PHONY: *

export NAME?=$(shell echo $(shell basename $(shell pwd)) | awk '{print tolower($0)}')

$(NAME): image
	@docker-compose up -d clickhouse prometheus redis postgres superset
	@docker-compose run $(NAME) /bin/bash

image:
	@docker-compose build $(NAME)

clean:
	@docker-compose down
	@rm -rf ch-data ch-log ._ch-data ._ch-log pr-data pg-data ._pg-data redis-data ._redis-data

info:
	@docker-compose logs
	@docker-compose ps

ss-u:
	@docker-compose up -d superset

ss-i:
	@docker-compose exec superset superset-init
