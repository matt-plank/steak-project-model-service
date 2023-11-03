FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY model_service model_service
COPY pyproject.toml pyproject.toml
RUN python -m pip install .

CMD ["model-service"]
