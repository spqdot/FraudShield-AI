
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
COPY pyproject.toml .
COPY src/ ./src/

RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir .

COPY models/ ./models/

EXPOSE 8000

CMD ["uvicorn", "fraudshield.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
