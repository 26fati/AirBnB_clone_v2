#!/usr/bin/python3
# a script that starts a Flask web application

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    ''' display hello hbnb'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    ''' display hbnb'''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_text(text):
    ''' display text'''
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text="is cool"):
    ''' display c with text'''
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    ''' display a number'''
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_number_template(n):
    ''' display a number with template'''
    return render_template('5-number.html', argument=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
