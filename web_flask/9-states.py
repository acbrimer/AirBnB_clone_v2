#!/usr/bin/python3
""" Console Module """
from models.__init__ import storage
from models.state import State

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/states')
def states_list():
    states = list(storage.all(State).values())
    return render_template('9-states.html', states=states, req_type='list')


@app.route('/states/<id>')
def state_get(id):
    states = storage.all(State)
    state = None
    if "State.{}".format(id) in states:
        state = states["State.{}".format(id)]
    print(state)
    return render_template('9-states.html', states=state, req_type='one')


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port="5000")
