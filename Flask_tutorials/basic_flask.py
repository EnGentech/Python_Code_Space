#!/usr/bin/python3
"""My first flask script"""

from flask import Flask, redirect, url_for, render_template
import re
pattern = re.compile("_")

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def name(text):
    new = pattern.sub(" ", text)
    return "C {}".format(new)


@app.route("/python", strict_slashes=False)
def python():
    return "Python is cool"


@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    if text == "is cool":
        return redirect(url_for("python"))
    else:
        new = pattern.sub(" ", text)
        return "Python {}".format(new)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_temp(n):
    if n:
        return render_template("number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    if n:
        return render_template("number.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)