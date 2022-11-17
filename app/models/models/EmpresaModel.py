from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, BooleanField
from wtforms.validators import DataRequired

class CadastroEmpresaForm(FlaskForm):
    nome = StringField("name", validators=[DataRequired()])
    email = EmailField("email", validators=[DataRequired()])
    cnpj = StringField("senha", validators=[DataRequired()])
    

