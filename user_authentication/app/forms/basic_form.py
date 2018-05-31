"""
Creating Basic form Validation and Queries.

The script below is an example of how to screate, validate, regex, options, and
other useful information when creating we parts for a website.

"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Regexp, DataRequired

# This is the Regex to validate name variables mostly for first and last
name_regex_validator = Regexp(
    "^[a-zA-Z]([a-zA-Z ']{2,250})$",
    message="Only letters, \"-\" and ' allowed, should start with a letter\
    , and be 2 to 250 characters"
)
# This will allow only zero(0) or one (1) chars to be entered
one_char_regex_validator = Regexp(
    "^[a-zA-Z]([a-zA-Z]{0,1})$",
    message="Only one (1) letter allowed for middle initial."
)
# Validationg an email Address
email_regex_validator = Regexp(
    "\A[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@\
    (?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?",
    message="Email Does Not Match"
)


class BasicForm(FlaskForm):
    """
    Basic Form.

    This basic form shows how to create inputs, dropdown,
    radio, validation and more.
    """

    # SubmitField to sned the data
    submit = SubmitField("Send Email")
