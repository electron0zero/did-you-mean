# forms
from flask_wtf import Form
from wtforms import TextField, SubmitField, ValidationError, validators, BooleanField


class QueryForm(Form):
    search_key = TextField("Type and press Enter", [validators.Required("required")])
    title = BooleanField('Title', default=False)
    submit = SubmitField("Search")
