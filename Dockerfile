# Use the official Python slim image
FROM python:3.10-slim

# Install system dependencies needed for building Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    libatlas-base-dev \
    liblapack-dev \
    libblas-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /usr/bin/code


COPY ./pyproject.toml /usr/bin/code/pyproject.toml
COPY ./poetry.lock /usr/bin/code/poetry.lock
COPY ./index.md /usr/bin/code/index.md

# Install Poetry via pip
RUN pip install --upgrade pip \
    && pip install poetry

RUN poetry install --no-root --only=main

# Expose the necessary port
EXPOSE 7860

# Copy the rest of your application code
COPY . /usr/bin/code/

# Create a user and switch to it
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# Set the working directory for the user
WORKDIR $HOME/app

# Copy application code to the user's home directory
COPY --chown=user . $HOME/app

# Add health check for the application
HEALTHCHECK CMD curl --fail http://localhost:7860/_stcore/health

# Command to run your application
CMD poetry run streamlit run presidio_streamlit.py --server.port 7860 --server.address=0.0.0.0