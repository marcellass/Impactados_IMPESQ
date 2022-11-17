from app import db

class Empresa(db.Model):
    __tablename__ = "tbl_empresas"
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), unique=True)
    email = db.Column(db.String)
    cnpj = db.Column(db.String)

    # contrutor da classe
    def __init__(self, nome, email, cnpj):
        self.nome = nome
        self.email = email
        self.cnpj = cnpj

    # representacao
    # como a classe apresenta os registros
    def __repr__(self):

        empresas = [self.id, self.nome, self.email, self.cnpj]

        return "%r" % empresas
