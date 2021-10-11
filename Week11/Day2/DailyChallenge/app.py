import flask

app = flask.Flask(__name__)


@app.route('/')
def chapter():
    return flask.render_template('in-this-chapter.md')


@app.route("/exercises")
def exercises():
    return flask.render_template('exercises.md')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
