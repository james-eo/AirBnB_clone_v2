#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, render_template

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


@app.route("/number/<int:n>", strict_slashes=False)
def display_n(n):
    """Displays 'n is a number' only if n is integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_template(n):
    """Displays an HTML page with 'Number: n' if n is an integer."""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_or_odd(n):
    """Displays a HTML page only if n is an integer"""
    parity = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html", n=n, parity=parity)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
