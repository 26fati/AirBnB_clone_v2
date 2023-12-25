#!/usr/bin/python3
"""A script that starts a flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def display_cities_amenities():
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown_appcontext(exception=None):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
