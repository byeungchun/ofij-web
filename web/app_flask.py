# app_flask.py
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Flask allows you to return a string directly,
    # or render a more complex HTML template.
    # Here, we're embedding the HTML directly.
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Flask Hello</title>
            <style>
                body {
                    font-family: sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    min-height: 100vh;
                    margin: 0;
                    background-color: #f0f0f0;
                }
                h1 {
                    color: #333;
                }
            </style>
        </head>
        <body>
            <h1>Hello, World!</h1>
        </body>
        </html>
    """)

if __name__ == '__main__':
    # You can specify host and port here.
    # debug=True allows for automatic reloading on code changes
    # and provides a debugger in the browser for errors.
    app.run(debug=True, host='0.0.0.0', port=8080)