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

# WP42D-ROLLBACK-REPAIR: cache-bust the HF runtime image so the Space
# cannot keep running an image that still contains a stale mutated
# presidio_streamlit.py static-highlight block.
ENV SCRUB_ROLLBACK_REPAIR=20260613_0015

# Copy the current directory contents into the container at $HOME/app setting the owner to the user
COPY --chown=user . $HOME/app

# WP42D-ROLLBACK: disable the experimental static highlight preview startup patch.
# The patch caused repeated runtime errors in the Hugging Face Space and is parked
# until it can be redesigned without mutating presidio_streamlit.py at startup.
CMD ["sh", "-c", "python fix_streamlit_nested_expanders.py && python fix_streamlit_export_download_ux.py && python fix_streamlit_pdf_text_reinsert.py && streamlit run presidio_streamlit.py --server.port=7860 --server.address=0.0.0.0 --server.enableXsrfProtection=false --server.enableCORS=false"]
