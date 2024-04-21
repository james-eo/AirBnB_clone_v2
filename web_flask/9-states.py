#!/usr/bin/python3
""" Script to start a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """ Route to display a HTML page with all states """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)

    return render_template('9-templates.html', states=states)


@app.route('/states/<state_id>', strict_slashes=False)
def states_cities(state_id):
    """ Route to display a HTML page with cities of a state """
    state = storage.get(State, state_id)

    if state is None:
        return render_template('9-templates.html', not_found=True)

    cities = sorted(state.cities, key=lambda city: city.name)

    return render_template('9-templates.html', state=state, cities=cities)


@app.teardown_appcontext
def teardown_db(exception):
    """ Teardown method to close the storage """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
