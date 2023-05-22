from app import db
from app.models.EmpresaEntity import Empresa

class FormularioEntity(db.Model):

    __tablename__ = "tbl_formulario"
    
    id = db.Column(db.Integer, primary_key=True)
    empresa_id = db.Column(db.Integer, db.ForeignKey('tbl_empresas.id'))
    pesquisa_id = db.Column(db.Integer, db.ForeignKey('tbl_pesquisas.id'))
    pergunta = db.Column(db.String(255))

    def get_id(self):
        return str(self.id)

    # contrutor da classe
    def __init__(self, empresa_id, pesquisa_id, pergunta):
        self.empresa_id = empresa_id
        self.pesquisa_id = pesquisa_id
        self.pergunta = pergunta

        

    # representacao
    # como a classe apresenta os registros
    def __repr__(self):
        
        return '<FormularioEntity(id={}, empresa_id={}, pesquisa_id={}, pergunta={})>'.format(
        self.id, self.empresa_id, self.pesquisa_id, self.pergunta)



    