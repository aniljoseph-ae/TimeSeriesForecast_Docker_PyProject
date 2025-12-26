# docker/dl.Dockerfile

FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml .
COPY src/ src/

RUN pip install --upgrade pip && \
    pip install -e .[dl,mlops,notebooks]

CMD ["python"]
