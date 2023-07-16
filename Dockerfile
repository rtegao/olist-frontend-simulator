FROM python:3.10 as base

ENV PROJECT_LOCATION=/opt/frontend_simulator
WORKDIR $PROJECT_LOCATION

#define path to data(frames)
ENV DOCKER_ENV=True

#install poetry
FROM base as base-env

RUN curl -sSL https://install.python-poetry.org | python3 - --git https://github.com/python-poetry/poetry.git@master
ENV PATH="${PATH}:/root/.local/bin"
COPY poetry.lock pyproject.toml Makefile $PROJECT_LOCATION/
RUN make install

FROM base-env as frontend-simulator-production

COPY app.py settings.toml $PROJECT_LOCATION/
RUN sed -i "s/{{PATH_TYPE}}/${PATH_TYPE}/g" settings.toml
COPY data $PROJECT_LOCATION/data
COPY frontend_simulator $PROJECT_LOCATION/frontend_simulator
