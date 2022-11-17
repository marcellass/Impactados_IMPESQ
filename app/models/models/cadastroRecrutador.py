from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, BooleanField
from wtforms.validators import DataRequired

class CadastroRecrutadorForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    email = EmailField("email", validators=[DataRequired()])
    senha = PasswordField("senha", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")
    

