from flask import Flask, render_template
from models import storage


app = Flask(__name__, strict_slashes=False)


@app.route('/states')
def all_states():
    """ Route to display a HTML page with all states """
    all_states = storage.all(State)
    all_states = sorted(all_states, key=lambda state: state.name)
    return render_template('states.html', states=all_states)


@app.route('/states/<state_id>')
def state_details(state_id):
    """ Route to display a HTML page with cities of a state """
    state = storage.get(State, state_id)

    if state:
        cities = state.cities if hasattr(state,
                                         "cities") else state.get_cities()
        cities = sorted(cities, key=lambda city: city.name)
        return render_template('state_details.html',
                               state=state,
                               cities=cities
                               )
    else:
        return render_template('not_found.html')


@app.teardown_appcontext
def teardown_db(exception):
    """ Teardown method to close the storage """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
