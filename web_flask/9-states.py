#!/usr/bin/python3
"""Start a flask app"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', defaults={'id': None}, strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Display Html page with a list of all states"""
    states = storage.all(State)
    if id:
        id = 'State.' + id
    return render_template("9-states.html", states=states, id=id)


@app.teardown_appcontext
def close_storage(exception):
    """ close the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
