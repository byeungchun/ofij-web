#!/bin/bash

# Navigate to the application directory
# IMPORTANT: The path is updated to /web/ofij-web/web as requested.
cd /web/ofij-web/web

# Activate your virtual environment if you are using one
# If you don't use a virtual environment, you can comment out or remove these lines
# source venv/bin/activate

# Define log file paths
# Ensure these directories exist and are writable by the Gunicorn user
LOG_DIR="/web/log"
ACCESS_LOG="$LOG_DIR/access.log"
ERROR_LOG="$LOG_DIR/error.log"

# Create the log directory if it doesn't exist
mkdir -p "$LOG_DIR"

# Run Gunicorn
# --workers 3: Number of worker processes. Adjust based on your server's CPU cores.
# --bind 0.0.0.0:8080: Binds Gunicorn to all network interfaces on port 8080 as requested.
# app:app: Specifies the Flask application. 'app' is the module (app.py), and 'app' is the Flask instance name.
# --access-logfile: Specifies the file to which access logs will be written.
# --error-logfile: Specifies the file to which error logs will be written.
exec gunicorn --workers 1 \
              --bind 0.0.0.0:8080 \
              --access-logfile "$ACCESS_LOG" \
              --error-logfile "$ERROR_LOG" \
              app:app
