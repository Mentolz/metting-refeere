FROM python:3.6.13-slim-buster

ENV PATH="$PATH:/root/.poetry/bin"

# System deps:
RUN apt-get update \
  && apt-get install --no-install-recommends -y \
    bash \
    build-essential \
    curl \
    gettext \
    git \
    libpq-dev \
# Installing `poetry` package manager:
# https://github.com/python-poetry/poetry
  && curl -sSL 'https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py' | python \
  && poetry --version
# Cleaning cache:
#  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
#  && apt-get clean -y && rm -rf /var/lib/apt/lists/*

WORKDIR home/meeting-referee

COPY ./ ./

RUN poetry install

CMD poetry run python run.py
