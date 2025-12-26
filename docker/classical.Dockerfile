# docker/classical.Dockerfile

FROM python:3.10-slim

# System setup
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    git \
    graphviz \
    && rm -rf /var/lib/apt/lists/*

# Work directory
WORKDIR /app

# Copy package metadata
COPY pyproject.toml .
COPY src/ src/

# Install Python deps
RUN pip install --upgrade pip && \
    pip install -e .[classical,mlops,notebooks]

# Default command
CMD ["python"]
