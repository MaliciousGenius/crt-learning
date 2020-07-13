# базовый образ
FROM jupyter/minimal-notebook

# подпись
LABEL maintainer="Dmitriy Detkov"
LABEL email="maliciousgenius@gmail.com"
LABEL tel="+79604565686"

# повышение привелегий
USER root

# обновление
RUN apt-get update --quiet ; \
    apt-get upgrade --quiet --yes ;

# очистка кеша пакетного менеджера
RUN apt-get autoremove --yes ; \
    apt-get clean ; \
    rm -rf /var/lib/apt/lists/* ;

# понижение привелегий
USER $NB_UID

# CMD ["jupyter", "notebook", "--no-browser","--NotebookApp.token=''","--NotebookApp.password=''"]
