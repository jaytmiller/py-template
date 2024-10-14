ARG BASE_IMAGE_REPO
ARG BASE_IMAGE_NAME
#FROM python:3.11-slim
FROM ${BASE_IMAGE_REPO}${BASE_IMAGE_NAME}

ARG SERVER_URL="localhost:5050"
ARG SVC_UID={{PYT_PKG_NAME}}
ARG SVC_GID={{PYT_PKG_NAME}}

ENV SVC_UID=$SVC_UID
ENV SVC_GID=$SVC_GID
ENV SERVER_URL=$SERVER_URL
ENV BACKGROUND_LOGGING=1
ENV USE_SUDO=1

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y sudo

RUN python -m venv /usr/src/app/{{PYT_PKG_NAME}}/venv

WORKDIR /usr/src/app/{{PYT_PKG_NAME}}
COPY requirements.txt requirements.txt
RUN /usr/src/app/{{PYT_PKG_NAME}}/venv/bin/pip install --no-cache --upgrade pip
RUN /usr/src/app/{{PYT_PKG_NAME}}/venv/bin/pip install --no-cache -r requirements.txt
RUN /usr/src/app/{{PYT_PKG_NAME}}/venv/bin/pip install --no-cache .

RUN mkdir /services/{{PYT_PKG_NAME}}
WORKDIR /services/{{PYT_PKG_NAME}}
USER $SVC_UID

CMD /usr/src/app/{{PYT_PKG_NAME}}/venv/bin/hypercorn --bind ${SERVER_URL} {{PYT_PKG_NAME}}.service:app
