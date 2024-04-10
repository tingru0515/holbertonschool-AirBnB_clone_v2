#!/usr/bin/python3
"""flask model for route"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    return "C %s" % text.replace("_", " ")


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    return "Python %s" % text.replace("_", " ")


@app.route("/number/<n>", strict_slashes=False)
def n_number(n):
    try:
        number = int(n)
        return "%i is a number" % number
    except ValueError:
        return "Not a number", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
