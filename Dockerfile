FROM python:3.10.13-alpine 

ENV PYTHONDONTWRITEBYTECODE 1  
ENV PYTHONUNBUFFERED 1  

WORKDIR /home/app  
COPY ./pyproject.toml ./poetry.lock* ./  

RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock ./README.md ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# RUN poetry install  

# CMD ["ping", "127.0.0.1"]
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8085", "--reload"]
