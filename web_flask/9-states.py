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
    all_states = storage.all(State).values()
    data = []

    for state in all_states:
        item = {'state': state, 'cities': []}
        cities = state.cities
        if cities:
            sorted_cities = sorted(cities, key=lambda c: c.name)
            item['cities'] = sorted_cities
        data.append(item)

    if id:
        the_state = storage.get(State, id)
        if the_state:
            return render_template("9-states.html", the_state=the_state)
        else:
            return render_template("9-states.html", not_found=True)
    else:
        sorted_states = sorted(all_states, key=lambda s: s.name)
        return render_template("9-states.html", states=sorted_states)
    # all_states = storage.all(State).values()

    # if id:
    #     the_state = storage.get(State, id)
    #     if the_state:
    #         the_state.cities = sorted(the_state.cities,
    #                                   key=lambda city: city.name)
    #         return render_template("9-states.html", the_state=the_state)
    #     else:
    #         return render_template("9-states.html", not_found=True)
    # else:
    #     states = sorted(all_states, key=lambda state: state.name)
    #     return render_template("9-states.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
