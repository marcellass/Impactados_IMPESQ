from app import db


class Recutrador(db.Model):
    __tablename__ = "tbl_recrutador"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120))
    email = db.Column(db.String, unique=True)
    senha = db.Column(db.String)

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

        # contrutor da classe
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    # representacao
    # como a classe apresenta os registros
    def __repr__(self):
        return "<Recrutador %r>" % self.nome

