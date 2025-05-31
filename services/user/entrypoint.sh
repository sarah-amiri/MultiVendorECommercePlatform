#!/bin/bash

# Run migrations
alembic upgrade head

# Run the app
gunicorn -w 2 -k uvicorn.workers.UvicornWorker src.app.main:app -b 0.0.0.0:8001