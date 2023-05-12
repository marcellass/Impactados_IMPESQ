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
from app.controllers.utils import charts
import matplotlib.pyplot as plt
import numpy as np
import os



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
    
    pesquisas = Pesquisa.query.filter_by().all()
    pesquisas = len(pesquisas)

    empresas = Empresa.query.filter_by().all()
    empresas = len(empresas)

    convidados = Convidado.query.filter_by().all()
    convidados = len(convidados)

    servicos = Pesquisa.query.filter_by(tipoObjeto="servico").all()
    servicos = len(servicos) 
    
    produtos = Pesquisa.query.filter_by(tipoObjeto="produto").all()
    produtos = len(produtos)  
    
    tipos_de_pesquisa = ['Produto', 'Serviço']
    total_de_pesquisas = [produtos, servicos]

    ages = ['0 -18', '18-35', '35-70']
    idades = charts.faixaEtariaChart()

    return render_template('home.html', pesquisas=pesquisas, empresas=empresas, convidados=convidados, tipos_de_pesquisa=tipos_de_pesquisa, total_de_pesquisas=total_de_pesquisas, ages=ages, idades=idades)

@app.route("/logout")
def logout():
    logout_user()
    flash("Deslogado")
    return redirect(url_for("login"))

@app.route("/base")
def base():
    return render_template('base.html')


def handleId(id):
    empresa = id
    return empresa