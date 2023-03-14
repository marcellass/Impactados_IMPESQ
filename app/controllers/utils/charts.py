from app.models.PesquisaEntity import Pesquisa
from app import app, db, loginManager
def faixaEtariaChart():

    child = len(Pesquisa.query.filter_by(faixaEtaria='0-18').all())
    young = len(Pesquisa.query.filter_by(faixaEtaria='18-35').all())
    mature = len(Pesquisa.query.filter_by(faixaEtaria='35-70').all())

    
    total_idades = [child, young, mature]

    return total_idades
    
   

    
    