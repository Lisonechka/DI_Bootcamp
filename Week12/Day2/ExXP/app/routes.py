import flask
from app import app
import flask
from app import app
from app.forms import Form


@app.route('/', methods=("GET","POST"))
def index():
    form = Form()
    if form.validate_on_submit():
        city_name = form.city_name.data
        print("question:", city_name)
    return flask.render_template("index.html", form=form)