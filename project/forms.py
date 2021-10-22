from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, Email, InputRequired, Length

class MessageForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()], render_kw={'class': 'form-control'})
    email = StringField("Email: ", validators=[Email(),DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Применить")
