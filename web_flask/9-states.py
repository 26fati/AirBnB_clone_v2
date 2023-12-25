#!/usr/bin/python3
"""A script that starts a flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def display_states():
    states = storage.all(State)
    return render_template("9-states.html", states=states, mode="states")


@app.route("/states/<id>", strict_slashes=False)
def display_cities(id):
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html",
                                   state=state, mode="state.id")
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown_appcontext(exception=None):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
