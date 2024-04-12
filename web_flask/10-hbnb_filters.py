#!/usr/bin/python3
"""to start a flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    state_cities = []
    amenities = []
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda amen: amen.name)
    for state in states:
        item = {}
        item["state"] = state
        cities = sorted(state.cities, key=lambda city: city.name)
        item["cities"] = cities
        state_cities.append(item)
    for amenity in amenities:
        amenities.append(amenity.name)

    return render_template("10-hbnb_filters.html", state_cities=state_cities, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
