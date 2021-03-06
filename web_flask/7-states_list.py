#!/usr/bin/python3
""" Module for a simple flask app with single route """

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/states_list')
def states_list():
    states = list(storage.all(State).values())
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port="5000")
