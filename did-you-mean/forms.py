# forms
from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, ValidationError, validators


class QueryForm(FlaskForm):
    search_key = TextField("Type and press Enter", [validators.Required("required")])
    submit = SubmitField("Search")
