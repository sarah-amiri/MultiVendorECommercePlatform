FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

CMD ["gunicorn", "-w", "2", "-k", "uvicorn.workers.UvicornWorker", "src.app.main:app", "-b", "0.0.0.0:8002"]