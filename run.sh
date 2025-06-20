#!/bin/bash

# This script runs the Streamlit application for FinAI Insights.
# It ensures the application is accessible publicly within a container
# by binding to all network interfaces (0.0.0.0) and listening on port 8080.

# Define the directory where the Streamlit application file is located
APP_DIR="/web/ofij-web/web"

# Define the main Streamlit application file name
APP_FILE="app.py" # Updated file name

# Define the host and port for public access
HOST="0.0.0.0"
PORT="8080"

echo "Changing directory to $APP_DIR..."
cd "$APP_DIR" || { echo "Error: Failed to change directory to $APP_DIR. Exiting."; exit 1; }

echo "Starting FinAI Insights Streamlit application..."
echo "Access the application at http://${HOST}:${PORT}" # Note: This will show 0.0.0.0. In browser, use container IP or localhost.

# Execute the Streamlit command
streamlit run "$APP_FILE" \
    --server.port "$PORT" \
    --server.address "$HOST" \
    --server.enableCORS true \
    --server.enableXsrfProtection false
    # --server.enableCORS true is generally good for container deployments
    # --server.enableXsrfProtection false might be needed in some container setups,
    # but be aware of the security implications in a public-facing app.
    # For a simple informational site, it's often fine.
