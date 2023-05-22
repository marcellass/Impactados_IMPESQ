from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateTimeLocalField, RadioField
from wtforms.validators import DataRequired


class CadastroPesquisaModel(FlaskForm):

    tipoObjeto =  SelectField('tipoObjeto', choices=[('produto','Produto'),('servico','Serviço')], default='produto', validators=[DataRequired()])
    dataHoraPesquisa = DateTimeLocalField("dataHoraPesquisa", format="%Y-%m-%dT%H:%M", validators=[DataRequired()] )


    genero = SelectField("generos", choices=[('Masculino', 'Masculino'),('Feminino', 'Feminino'),('Ambos', 'Ambos')], validators=[DataRequired()])
    objetoPesquisa = StringField("objetoPesquisa", validators=[DataRequired()])
   
   
    faixaEtaria = RadioField("faixaEtaria",choices=[('0-18','0 - 18'),('18-35','18 - 35'),('35-70','35 - 70')], validators=[DataRequired()])
    classeEconomica = SelectField("classeEconomica", choices=[('A', 'A'),('B1', 'B1'),('B2', 'B2'),('C1', 'C1'),('C2', 'C2'),('DE', 'DE')], validators=[DataRequired()])
    

