from flask import Flask
# from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.models.models import cadastroRecrutador, login
from flask_login import LoginManager
from flask_react import React

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

app.config['REACT_FOLDER'] = 'client/build'
react = React(app)

migrate = Migrate(app, db)

loginManager = LoginManager()
loginManager.init_app(app)
# initialize the app with the extension
# db.init_app(app)

# mysql = MySQL()
# mysql.init_app(app)

from app.models import RecrutadorEntity, EmpresaEntity, PesquisaEntity, ConvidadoEntity
from app.models.models import login, cadastroRecrutador, PesquisaModel, EmpresaModel
from app.controllers import default, reactBackEnd

