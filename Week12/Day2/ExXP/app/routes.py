import flask
from app import app
from flask import flash


@app.route("/")
def index():
    return flask.render_template('index.html')
