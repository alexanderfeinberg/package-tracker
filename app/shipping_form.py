from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired
from ..map.map import map


def format_locations(map):
    location_list = [(key, key) for key in map.keys()]
    return location_list


class ShippingForm(FlaskForm):
    sender = StringField("Name of sender", validators=[DataRequired()])
    recipient = StringField("Name of recipient", validators=[DataRequired()])
    origin = SelectField("Shipping From", choices=format_locations(
        map), validators=[DataRequired()])
    destination = SelectField("Shipping To", choices=format_locations(
        map), validators=[DataRequired()])
    express = BooleanField("Express shipping?", validators=[DataRequired()])
    submit = SubmitField("Submit")
