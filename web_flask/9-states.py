#!/usr/bin/python3
""" Module for a simple flask app with single route """

# storage = __import__('Users/abrimerHome/Holberton/AirBnB_clone_v2/models').storage
# State = __import__('Users/abrimerHome/Holberton/AirBnB_clone_v2/models/states.py').State
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/states')
def states_list():
    states = list(storage.all(State).values())
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def state_get(id):
    states = storage.all(State)
    state = None
    if "State.{}".format(id) in states:
        state = states["State.{}"]
    return render_template('9-states.html', states=state)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port="5000")
