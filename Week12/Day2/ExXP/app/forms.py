import flask_wtf
import wtforms


class Form(flask_wtf.FlaskForm):
    city_name = wtforms.StringField("Your city is: ", [wtforms.validators.required(),
                                                       wtforms.validators.Length(min=2, max=15)])
    country = wtforms.StringField("Country is: ", [wtforms.validators.required()])
    inhabitants = wtforms.StringField("Number of inhabitants: ", [wtforms.validators.required()])
    area = wtforms.StringField("City’s area: ")
    submit = wtforms.SubmitField("Submit")
