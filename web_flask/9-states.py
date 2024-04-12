#!/usr/bin/python3
"""to start a flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_id(id=None):
    states = sorted(storage.all(State).values(), key=lambda state: state.name) if states else []
    the_state = None
    if id:
        the_state = next((state for state in states if state.id == id), None)
        if the_state is not None:
            the_state.cities = sorted(the_state.cities, key=lambda city:city.name)
        states = None
    return render_template("9-states.html", states=states, the_state=the_state)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
