FROM python:3.12.3-alpine3.19 AS dependencies
RUN apk update && apk add --update --no-cache bash
RUN addgroup -g 1000 alpine && adduser -u 1000 -G alpine -s /bin/bash -h /home/alpine -D alpine
USER alpine
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    POETRY_VIRTUALENVS_PATH="/home/alpine/.venv"
RUN pip install --upgrade pip
RUN python3 -m pip install --user pipx
RUN python3 -m pipx ensurepath
ENV PATH=/home/alpine/.local/bin:$PATH
RUN python3 -m pipx install poetry
USER root

FROM dependencies AS develop
WORKDIR /srv
RUN chmod 777 /srv
USER alpine

FROM dependencies
ARG BUILD_DATE
ARG BUILD_VERSION
LABEL org.label-schema.name="posts-api"
LABEL org.label-schema.vcs-url="https://github.com/cloudstart-io/posts-api"
LABEL org.label-schema.vcs-ref=${BUILD_VERSION}
LABEL org.label-schema.build-date=${BUILD_DATE}
WORKDIR /srv
COPY src app
COPY poetry.lock /srv/poetry.lock
COPY pyproject.toml /srv/pyproject.toml
RUN chown -R alpine:alpine /srv/app
USER alpine
RUN poetry install --without dev --no-interaction --no-ansi -vvv && rm -rf $POETRY_CACHE_DIR
CMD ['sh', '-c', 'poetry run gunicorn -k uvicorn.workers.UvicornWorker -c gunicorn_conf.py app.main:app']
