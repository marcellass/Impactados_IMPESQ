from app import app, db, loginManager
from flask import render_template, flash, redirect, url_for, request
from app.models.RecrutadorEntity import Recutrador
from app.models.models.login import LoginForm
from app.models.models.cadastroRecrutador import CadastroRecrutadorForm
from flask_login import login_user, logout_user
from app.models.models.EmpresaModel import CadastroEmpresaForm
from app.models.EmpresaEntity import Empresa



@loginManager.user_loader
def load_user(id):
    return Recutrador.query.filter_by(id=id).first()

@app.route("/cadastrar", methods=["GET","POST"])
def cadastrar():
    form = CadastroRecrutadorForm()
    if form.validate_on_submit():
        recrutador = Recutrador(form.name.data, form.email.data, form.senha.data)
        db.session.add(recrutador)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        print(form.errors)
    return render_template('cadastro_recrutador.html', form=form)

    
@app.route("/")
@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        recrutador = Recutrador.query.filter_by(email=form.email.data).first()
        if recrutador and recrutador.senha == form.senha.data:
            login_user(recrutador)
            flash("Logado!")
            return redirect(url_for('home'))
        else:
            flash("Login inválido")
    else:
        print(form.errors)
    return render_template('login.html', form=form)



@app.route("/home")
def home():
    read = Recutrador.query.filter_by(nome="admin").first()

    return render_template('index.html', user=read)

@app.route("/logout")
def logout():
    logout_user()
    flash("Deslogado")
    return redirect(url_for("login"))


@app.route("/cadastrar/empresa", methods=["GET","POST"])
def cadastrarEmpresa():
    form = CadastroEmpresaForm()
    if form.validate_on_submit():
        empresa = Empresa(form.nome.data, form.email.data, form.cnpj.data)
        db.session.add(empresa)
        db.session.commit()
        return redirect(url_for('cadastrarEmpresa'))
    else:
        print(form.errors)
    return render_template('cadastro_empresa.html', form=form)


@app.route("/listar/empresa", methods=["GET","POST"])
def listarEmpresa():

    empresas = Empresa.query.filter_by().all()

    return render_template('empresas_cadastradas.html', empresas= empresas)


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


@app.route("/base")
def base():
    return render_template('base.html')
