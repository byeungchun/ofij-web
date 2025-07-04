# app.py

from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def index():
    """
    Renders the main index.html template for the home page.
    This function serves as the entry point for the website.
    """
    return render_template('index.html')

# Define the route for the data page
@app.route('/data')
def data():
    """
    Renders the data.html template.
    This function handles requests for the /data URL.
    """
    return render_template('data.html')

# Run the Flask application
if __name__ == '__main__':
    # When running the application directly, start the Flask development server.
    # debug=True allows for automatic reloading on code changes and provides a debugger.
    # It should be set to False in a production environment.
    app.run(debug=True)
