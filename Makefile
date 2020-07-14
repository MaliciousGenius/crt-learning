.PHONY: *

export NAME?=$(shell echo $(shell basename $(shell pwd)) | awk '{print tolower($0)}')

$(NAME): image
	@docker-compose up -d clickhouse
	@docker-compose run $(NAME) /bin/bash

image:
	@docker-compose build $(NAME)

down:
	@docker-compose down

info:
	@docker-compose logs
	@docker-compose ps
