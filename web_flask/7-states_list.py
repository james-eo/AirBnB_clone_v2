#!/usr/bin/python3
""" Script to start a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State

'''
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Route to display a HTML page with all states """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)

    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """ Teardown method to close the storage """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
'''

app = Flask(__name__)
app.config['STRICT_SLASHES'] = False


@app.teardown_appcontext
def teardown_db(exception):
    """ Teardown method to close the storage """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Route to display a HTML page with all states """
    states = storage.all(State)
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
