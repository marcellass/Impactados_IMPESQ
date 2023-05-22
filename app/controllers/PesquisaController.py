from app import app, db, loginManager
from flask import render_template, flash, redirect, url_for, request, send_from_directory
from app.models.RecrutadorEntity import Recutrador
from app.models.models.login import LoginForm
from app.models.models.cadastroRecrutador import CadastroRecrutadorForm
from flask_login import login_user, logout_user
from app.models.EmpresaEntity import Empresa
from app.models.models.PesquisaModel import CadastroPesquisaModel
from app.models.PesquisaEntity import Pesquisa
from app.models.ConvidadoEntity import Convidado


if __name__ == '__main__':
    app.run()

@app.route("/selecionar/empresa", methods=["GET","POST"])
def selecionarEmpresa():
    empresas = Empresa.query.filter_by().all()
    if request.method == 'POST':
        idEmpresa = request.form['id']
        return redirect(url_for('cadastrarPesquisa', idEmpresa=idEmpresa))
    return render_template('selecionar_empresa.html', empresas=empresas)


@app.route("/cadastrar/pesquisa/<idEmpresa>", methods=["GET","POST"])
@app.route("/cadastrar/pesquisa", methods=["GET","POST"])
def cadastrarPesquisa(idEmpresa):
    idEmpresa = idEmpresa
    form = CadastroPesquisaModel()


    if form.validate_on_submit():
        pesquisa = Pesquisa(idEmpresa=idEmpresa, objetoPesquisa=form.objetoPesquisa.data,
        tipoObjeto=form.tipoObjeto.data, dataHoraPesquisa=form.dataHoraPesquisa.data, generos=form.genero.data,
        classeEconomica=form.classeEconomica.data, faixaEtaria=form.faixaEtaria.data)
        db.session.add(pesquisa)
        db.session.commit()
        idPesquisa = pesquisa.id
        return redirect(url_for('novoFormulario', idEmpresa=idEmpresa, idPesquisa=idPesquisa))
    else:
         print(form.errors)
    return render_template('cadastro_pesquisa.html', form=form, idEmpresa=idEmpresa)


@app.route("/listar/pesquisas", methods=["GET","POST"])
def listarPesquisas():
    empresa = request.args.get('empresa')
    objetoPesquisa = request.args.get('objetoPesquisa')
    tipoObjeto = request.args.get('tipoObjeto')
    dataEHora = request.args.get('dataEHora')
    genero =  request.args.get('genero')
    faixaEtaria =  request.args.get('faixaEtaria')
    classeEconomica = request.args.get('classeEconomica')

    query = Pesquisa.query.filter_by()
    queryEmpresa = Empresa.query.filter_by()

    if empresa:
        queryEmpresa = queryEmpresa.filter(Empresa.nome == empresa)
        idEmpresa = queryEmpresa.first()
        query = query.filter(Pesquisa.idEmpresa == idEmpresa.id)
    if objetoPesquisa:
        query = query.filter(Pesquisa.objetoPesquisa == objetoPesquisa)
    if tipoObjeto:
        query = query.filter(Pesquisa.tipoObjeto == tipoObjeto)
    if dataEHora:
        query = query.filter(Pesquisa.dataHoraPesquisa == dataEHora)
    if genero:
        query = query.filter(Pesquisa.generos == genero)
    if faixaEtaria:
        query = query.filter(Pesquisa.faixaEtaria == faixaEtaria)
    if classeEconomica:
        query = query.filter(Pesquisa.classeEconomica == classeEconomica)
    

   

    pesquisas = query.all()
    empresas = queryEmpresa.all()


    
    return render_template('listar_pesquisa.html', pesquisas=pesquisas, empresas=empresas)

