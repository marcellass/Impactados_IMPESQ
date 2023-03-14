from app import db
from app.models.EmpresaEntity import Empresa

class Pesquisa(db.Model):

    __tablename__ = "tbl_pesquisas"
    
    id = db.Column(db.Integer, primary_key=True)
    #Se nao conseguir fazer a chave estrangeira, improvise criando um campo chamado idempresa e passe o id da empresa. 
    # e quando for adicionar passe o id apos selecionar pelo id
    # eh necessario fazer um flask db upgrade
    idEmpresa = db.Column(db.Integer)
    objetoPesquisa = db.Column(db.String)
    tipoObjeto = db.Column(db.String)
    dataHoraPesquisa = db.Column(db.String)
    generos = db.Column(db.String)
    faixaEtaria = db.Column(db.String)
    classeEconomica = db.Column(db.String)

    def get_id(self):
        return str(self.id)

    # contrutor da classe
    def __init__(self, idEmpresa, objetoPesquisa, tipoObjeto, dataHoraPesquisa, generos, faixaEtaria,  classeEconomica):
        self.idEmpresa = idEmpresa
        self.objetoPesquisa = objetoPesquisa
        self.tipoObjeto = tipoObjeto
        self.dataHoraPesquisa = dataHoraPesquisa 
        self.generos = generos
        self.faixaEtaria = faixaEtaria 
        self.classeEconomica = classeEconomica
        

    # representacao
    # como a classe apresenta os registros
    def __repr__(self):
        pesquisas = [self.id, self.idEmpresa, self.objetoPesquisa, self.tipoObjeto, self.dataHoraPesquisa, self.generos, self.faixaEtaria, self.classeEconomica]
        
        return "%r" % pesquisas



    