#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!' when accessing the root URL."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Displays 'HBNB' when accessing the /hbnb route."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_text(text):
    """Displays 'C ' followed by processed text"""
    processed_text = text.replace("_", " ")
    return f"C {processed_text}"


@app.route('/python/', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def dispaly_python(text='is cool'):
    """Displays python, followed by the value of the text variable"""
    processed_text = text.replace("_", " ")
    return f"Python {processed_text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
