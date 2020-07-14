.PHONY: *

# переменные
export NAME?=$(shell echo $(shell basename $(shell pwd)) | awk '{print tolower($0)}')

# рантайм - цель по умолчанию
$(NAME): image container

# установить и запустить контейнер
container:
	@docker-compose up -d

# собрать образ
image:
	@docker-compose build

# очистить
clean:
	@docker-compose down

# журнал & информация
info:
	@docker-compose logs
	@docker-compose ps
