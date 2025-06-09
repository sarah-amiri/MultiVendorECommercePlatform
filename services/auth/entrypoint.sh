#!/bin/bash

# Run the app
gunicorn -w 2 -k uvicorn.workers.UvicornWorker src.app.main:app -b 0.0.0.0:8002