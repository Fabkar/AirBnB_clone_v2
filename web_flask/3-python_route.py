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
    return 'HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def Nofound_message(text):
    """Function that return message depend of route
    in this case is no found"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonIs(text=''):
    """Function that return a massege depend of route
    by python is cool"""
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    """In each localhost cases the port 5000 is default"""
    app.run(host='0.0.0.0', port="5000")
