#!/usr/bin/python3
""" Module for a simple flask app with single route """


from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port="5000")
