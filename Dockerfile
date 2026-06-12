# Use the official Python 3.9 image
FROM python:3.10

# Set the working directory to /code
WORKDIR /code

# Install system dependencies required for building Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /code
COPY ./pyproject.toml /code/pyproject.toml
COPY ./poetry.lock /code/poetry.lock
COPY ./index.md /code/index.md

# Install requirements.txt
RUN pip install --upgrade pip setuptools wheel

RUN pip install "poetry==1.8.5"

ENV POETRY_VIRTUALENVS_CREATE=false

RUN poetry install --no-root

RUN pip install --upgrade "packaging>=24.2,<27"

RUN pip install --no-cache-dir python-docx pymupdf reportlab pypdf

# Set up a new user named "user" with user ID 1000
RUN useradd -m -u 1000 user
# Switch to the "user" user
USER user
# Set home to the user's home directory
ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH

# Set the working directory to the user's home directory
WORKDIR $HOME/app

# Copy the current directory contents into the container at $HOME/app setting the owner to the user
COPY --chown=user . $HOME/app

CMD ["sh", "-c", "python fix_streamlit_nested_expanders.py && python fix_streamlit_pdf_text_reinsert.py && python fix_streamlit_static_highlight_preview.py && streamlit run presidio_streamlit.py --server.port=7860 --server.address=0.0.0.0 --server.enableXsrfProtection=false --server.enableCORS=false"]
