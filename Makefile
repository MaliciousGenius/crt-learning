.PHONY: *

# переменные
export NAME?=$(shell echo $(shell basename $(shell pwd)) | awk '{print tolower($0)}')

# рантайм - цель по умолчанию
$(NAME): clean image container
	# @docker-compose exec $(NAME) /bin/bash

# установить и запустить контейнер
container:
	@docker-compose up -d

# собрать образ
image:
	@docker-compose build --force-rm --no-cache --pull $(NAME)

# очистить
clean:
	@docker-compose down

# журнал & информация
info:
	@docker-compose logs
	@docker-compose ps

superset-init:
	docker-compose exec superset superset-init
