#!/usr/bin/python3
"""flask model for route"""
from flask import Flask, render_template

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


@app.route("/python/", defaults="is cool", strict_slashes=False)
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


@app.route("/number_template/<n>", strict_slashes=False)
def html_page(n):
    try:
        number = int(n)
        return render_template("5-number.html", n=number)
    except ValueError:
        return "Not a number", 404


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def odd_even_html(n):
    try:
        number = int(n)
        if number % 2 == 1:
            return render_template("6-number_odd_or_even.html",
                                   n=number, odd_or_even="odd")
        else:
            return render_template("6-number_odd_or_even.html",
                                   n=number, odd_or_even="even")
    except ValueError:
        return "Not a number", 404


app.run(host="0.0.0.0", port=5000)
