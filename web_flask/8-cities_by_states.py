#!/usr/bin/python3
""" Script to start a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Route to display a HTML page with all states and cities """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)

    cities_by_state = {}

    for state in states:
        cities = sorted(state.cities, key=lambda city: city.name)
        cities_by_state[state] = cities

    return render_template('8-cities_by_states.html', states=cities_by_state)


@app.teardown_appcontext
def teardown_db(exception):
    """ Teardown method to close the storage """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
