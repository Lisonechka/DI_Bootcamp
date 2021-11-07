import flask_wtf
import wtforms


class Form(flask_wtf.FlaskForm):
    ask = wtforms.StringField("Name")
    submit = wtforms.SubmitField("Submit")
