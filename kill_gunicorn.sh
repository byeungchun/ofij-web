#!/bin/bash
# Kill the Gunicorn process running app:app on port 8080

# Find the Gunicorn process running app:app on port 8080
PID=$(ps aux | grep 'gunicorn' | grep 'app:app' | grep '0.0.0.0:8080' | grep -v grep | awk '{print $2}')

if [ -z "$PID" ]; then
  echo "No Gunicorn process found running app:app on port 8080."
  exit 1
else
  echo "Killing Gunicorn process with PID: $PID"
  kill $PID
  echo "Process killed."
fi
