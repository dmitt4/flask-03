from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.fields.core import SelectField, IntegerField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, Email, InputRequired, Length

class CalcForm(FlaskForm):
    x =  IntegerField("X", validators=[DataRequired()], render_kw={'class': 'form-control'})
    oper = SelectField("oper", validators=[DataRequired()], choices=[('+', '+'), ('-', '-'), ('*', '*'), ('/', ':'), ('**', '**')], render_kw={'class': 'form-control'})
    y = IntegerField("Y", validators=[DataRequired()], render_kw={'class': 'form-control'})
    submit = SubmitField("ОК")

class MessageForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()], render_kw={'class': 'form-control'})
    email = StringField("Email: ", validators=[Email(),DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Применить")
