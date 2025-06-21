#!/bin/bash

# Navigate to the application directory
# IMPORTANT: The path is updated to /web/ofij-web/web as requested.
cd /web/ofij-web/web

# Activate your virtual environment if you are using one
# If you don't use a virtual environment, you can comment out or remove these lines
# source venv/bin/activate

# Run Gunicorn
# --workers 3: Number of worker processes. Adjust based on your server's CPU cores.
# --bind 0.0.0.0:8080: Binds Gunicorn to all network interfaces on port 8080 as requested.
# app:app: Specifies the Flask application. 'app' is the module (app.py), and 'app' is the Flask instance name.
exec gunicorn --workers 3 --bind 0.0.0.0:8080 app:app
