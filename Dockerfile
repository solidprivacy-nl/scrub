FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    libatlas-base-dev \
    liblapack-dev \
    libblas-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code


# Poetry
RUN pip install --upgrade pip \
    && pip install poetry

COPY pyproject.toml poetry.lock /code/

RUN poetry install --no-dev


EXPOSE 7860

COPY . /code

RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

COPY --chown=user . $HOME/app

HEALTHCHECK CMD curl --fail http://localhost:7860/_stcore/health

CMD ["poetry", "run", "python", "-m", "streamlit", "run", "presidio_streamlit.py", "--server.port=7860", "--server.address=0.0.0.0"]
