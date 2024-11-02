# Use the official Python slim image
FROM python:3.10-slim

# Create a user and set permissions
RUN useradd -m -u 1000 user && mkdir -p /app && chown -R user:user /app

# Set working directory to /app and switch to the user
WORKDIR /app
USER user

# Install system dependencies needed for building Python packages (as root)
USER root
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    libatlas-base-dev \
    liblapack-dev \
    libblas-dev \
    && rm -rf /var/lib/apt/lists/*

# Switch back to the user to avoid permission issues
USER user

# Copy pyproject.toml and poetry.lock first for dependency installation
COPY --chown=user:user pyproject.toml poetry.lock /app/

# Install Poetry via pip
RUN pip install --upgrade pip && pip install poetry

# Install dependencies without installing the project root package itself
RUN poetry install --no-root --only=main

# Expose the necessary port
EXPOSE 7860

# Copy the rest of your application code to the container
COPY --chown=user:user . /app/

# Add health check for the application
HEALTHCHECK CMD curl --fail http://localhost:7860/_stcore/health

# Run the application using Poetry
CMD ["poetry", "run", "streamlit", "run", "presidio_streamlit.py", "--server.port=7860", "--server.address=0.0.0.0"]
