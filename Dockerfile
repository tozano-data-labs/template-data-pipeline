FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/pipelines/src

WORKDIR /app

COPY pipelines/requirements.txt ./pipelines/requirements.txt
RUN pip install --no-cache-dir -r pipelines/requirements.txt

COPY pipelines ./pipelines

CMD ["python", "-m", "pipeline.main", \
     "--input", "pipelines/exemples/source.csv", \
     "--output", "out/result.csv"]
