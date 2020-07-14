# базовый образ
FROM ubuntu

# подпись
LABEL maintainer="Dmitriy Detkov"
LABEL email="maliciousgenius@gmail.com"
LABEL tel="+79604565686"

# переменные
ENV DEBIAN_FRONTEND=noninteractive

# обновление
RUN apt-get update --quiet ; \
    apt-get upgrade --quiet --yes ;

# установка дополнительных пакетов
RUN apt-get install --quiet --yes --no-install-recommends \
        ca-certificates \
        apt-transport-https \
        software-properties-common \
        bash \
        openssl ;

# очистка кеша пакетного менеджера
RUN apt-get autoremove --yes ; \
    apt-get clean ; \
    rm -rf /var/lib/apt/lists/* ;
