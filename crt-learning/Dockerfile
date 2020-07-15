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
        bash bash-completion ;

# установка python 3 и его компонент
RUN apt-get install --quiet --yes --no-install-recommends \
        python3-pip \
        python3-numpy \
        python3-pandas ;

# установка clickhouse-driver
RUN pip3 install clickhouse-driver pandahouse

# очистка кеша пакетного менеджера
RUN apt-get autoremove --yes ; \
    apt-get clean ; \
    rm -rf /var/lib/apt/lists/* ;

WORKDIR /crt-scripts
