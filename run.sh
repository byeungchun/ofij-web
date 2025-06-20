#!/bin/bash

# This script runs the Flask application for FinAI Insights.
# It ensures the application is accessible publicly within a container
# by binding to all network interfaces (0.0.0.0) and listening on port 8080.

# Define the directory where the Flask application file is located
APP_DIR="/web/ofij-web/web"

# Define the main Flask application file name
APP_FILE="app.py"

# Define the host and port for public access
HOST="0.0.0.0"
PORT="8080"

echo "Changing directory to $APP_DIR..."
cd "$APP_DIR" || { echo "Error: Failed to change directory to $APP_DIR. Exiting."; exit 1; }

echo "Starting FinAI Insights Flask application..."
echo "Access the application at http://${HOST}:${PORT}"

# Execute the Flask command
export FLASK_APP="$APP_FILE"
export FLASK_RUN_HOST="$HOST"
export FLASK_RUN_PORT="$PORT"
flask run
