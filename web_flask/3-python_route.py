#!/usr/bin/python3
""" Module for 3-python_route """

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/<text>')
def c(text='is_cool'):
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port="5000")
