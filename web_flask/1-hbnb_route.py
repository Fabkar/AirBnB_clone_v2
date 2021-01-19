#!/usr/bin/python3
""" Start a flask app"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def first_greeting():
    """Function that return message depend of route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_message():
    """Function that return message depend of route"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
