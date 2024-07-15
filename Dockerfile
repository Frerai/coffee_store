FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev

COPY . /app

ENV PYTHONUNBUFFERED 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8100"]

