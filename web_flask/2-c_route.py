#!/usr/bin/python3
''' a script that starts a Flask web application '''

from flask import Flask

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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
