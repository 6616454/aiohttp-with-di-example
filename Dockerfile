FROM python:3.10-slim as build_app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY poetry.lock pyproject.toml ./

RUN python -m pip install --upgrade pip && pip install poetry && poetry config virtualenvs.create false


COPY . /app

FROM build_app as prod

RUN poetry install --without dev

EXPOSE 8080

CMD alembic upgrade head && python -m src.presentation.api.app