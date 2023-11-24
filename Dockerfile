FROM python:3.10.13-alpine 

ENV PYTHONDONTWRITEBYTECODE 1  
ENV PYTHONUNBUFFERED 1  

WORKDIR /home/app  
COPY ./pyproject.toml ./poetry.lock* ./  

RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock ./README.md ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi