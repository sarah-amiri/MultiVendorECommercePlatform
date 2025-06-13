#!/bin/bash

# Set variables
NUM_WORKERS=${NUM_WORKERS:-2}
APP_PORT=${APP_PORT_EXPOSE:-8003}

# Run the app
gunicorn -w $NUM_WORKERS -k uvicorn.workers.UvicornWorker src.app.main:app -b 0.0.0.0:$APP_PORT