from app import app, db, loginManager 
from flask import render_template, flash, redirect, url_for, request, send_from_directory
from app.models.EmpresaEntity import Empresa
from app.models.models.EmpresaModel import CadastroEmpresaForm


@app.route("/cadastrar/empresa", methods=["GET","POST"])
def cadastrarEmpresa():
    form = CadastroEmpresaForm()
    if form.validate_on_submit():
        empresa = Empresa(form.nome.data, form.email.data, form.cnpj.data)
        db.session.add(empresa)
        db.session.commit()
        return redirect(url_for('listarEmpresa'))
    else:
        print(form.errors)
    return render_template('cadastro_empresa.html', form=form)


@app.route("/listar/empresa", methods=["GET","POST"])
def listarEmpresa():
    nome = request.args.get('nome')
    email = request.args.get('email')
    cnpj = request.args.get('CNPJ')

    query = Empresa.query.filter_by()

    if nome:
        query = query.filter(Empresa.nome == nome)

    if email:
        query = query.filter(Empresa.email == email)

    if cnpj:
        query = query.filter(Empresa.cnpj == cnpj)

    empresas = query.all()

    return render_template('empresas_cadastradas.html', empresas=empresas)


@app.route("/atualizar/empresa", methods=["GET","POST"])
def atualizarEmpresa():
    form = CadastroEmpresaForm()
    id = request.form['id']
    empresaAntiga = Empresa.query.filter_by(id=id).first()
    if form.validate_on_submit():
        empresa = Empresa.query.filter_by(id=id).first()
        empresa.nome = form.nome.data
        empresa.cnpj = form.cnpj.data
        empresa.email = form.email.data
        db.session.commit()
        return redirect(url_for('listarEmpresa'))
    else:
        print(form.errors)
    return render_template('atualizar_empresa.html', form=form, empresaAntiga = empresaAntiga)
