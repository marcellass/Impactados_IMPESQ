from app import app, db, loginManager
from flask import render_template, flash, redirect, url_for, request
from app.models.RecrutadorEntity import Recutrador
from app.models.models.login import LoginForm
from app.models.models.cadastroRecrutador import CadastroRecrutadorForm
from flask_login import login_user, logout_user
from app.models.models.EmpresaModel import CadastroEmpresaForm
from app.models.EmpresaEntity import Empresa
from app.models.models.PesquisaModel import CadastroPesquisaModel
from app.models.PesquisaEntity import Pesquisa
from app.models.ConvidadoEntity import Convidado
from app.controllers.utils.utils import calculaCriterio

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

    return render_template('index.html', pesquisas=pesquisas, empresas=empresas, convidados=convidados)

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
        return redirect(url_for('listarPesquisas'))
    else:
         print(form.errors)
    return render_template('cadastro_pesquisa.html', form=form, idEmpresa=idEmpresa)


@app.route("/listar/pesquisas", methods=["GET","POST"])
def listarPesquisas():

    pesquisas = Pesquisa.query.filter_by().all()
    empresas = Empresa.query.filter_by().all()
    
    return render_template('listar_pesquisa.html', pesquisas=pesquisas, empresas=empresas)


@app.route('/cadastrar/convidado', methods=['POST', 'GET'])
def convidado():
    if request.method == 'POST':
        nomeConvidado = str(request.form['nomeConvidado'])
        sobrenomeConvidado = str(request.form['sobrenomeConvidado'])
        datanasc = str(request.form['datanasc'])
        rgConvidado = str(request.form['rgConvidado'])
        ufConvidado = str(request.form['ufConvidado'])
        cpfConvidado = str(request.form['cpfConvidado'])
        enderecoConvidado = str(request.form['enderecoConvidado'])
        bairroConvidado = str(request.form['bairroConvidado'])
        cidadeConvidado = str(request.form['cidadeConvidado'])
        cepConvidado = str(request.form['cepConvidado'])
        zonaConvidado = str(request.form['zonaConvidado'])
        formacaoConvidado = str(request.form['formacaoConvidado'])
        escolaridadeConvidado = str(request.form['escolaridadeConvidado'])
        ano_escolaridade = str(request.form['ano_escolaridade'])
        periodoConvidado = str(request.form['periodoConvidado'])
        estadoCivilConvidado = str(request.form['estadoCivilConvidado'])
        filhoConvidado = str(request.form['filhoConvidado'])
        primeiroFilho = str(request.form['primeiroFilho'])
        segundoFilho = str(request.form['segundoFilho'])
        nascimentoPrimeiroFilho = str(request.form['nascimentoPrimeiroFilho'])
        nascimentoSegundoFilho = str(request.form['nascimentoSegundoFilho'])
        trabalhoConvidado = str(request.form['trabalhoConvidado'])
        horarioTrabalho = str(request.form['horarioTrabalho'])
        empresaConvidado = str(request.form['empresaConvidado'])
        ramoConvidado = str(request.form['ramoConvidado'])
        telefoneEmpresa = str(request.form['telefoneEmpresa'])
        telefoneResidencial = str(request.form['telefoneResidencial'])
        celularConvidado = str(request.form['celularConvidado'])
        operadoraConvidado = str(request.form['operadoraConvidado'])
        opcaoOperadora = str(request.form['opcaoOperadora'])
        emailConvidado = str(request.form['emailConvidado'])
        pesquisaMercado = str(request.form['pesquisaMercado'])
        mktPubli = str(request.form['mktPubli'])
        rjrTv = str(request.form['rjrTv'])
        participouPesquisa = str(request.form['participouPesquisa'])
        tipoPesquisa1 = request.form.getlist('tipoPesquisa')
        tipoPesquisa =' '.join(map(str,tipoPesquisa1))
        dataUltimaPesquisa = str(request.form['dataUltimaPesquisa'])
        assuntoUltimaPesquisa = str(request.form['assuntoUltimaPesquisa'])
        geladeira = int(request.form['geladeira'])
        banheiro = int(request.form['banheiro'])
        freezer = int(request.form['freezer'])
        microondas = int(request.form['microondas'])
        lavaloucas = int(request.form['lavaloucas']) 
        maquinaroupa = int(request.form['maquinaroupa'])
        secarroupas = int(request.form['secarroupas'])
        empregado = int(request.form['empregado'])
        computador = int(request.form['computador'])
        aguaencanada = int(request.form['aguaencanada'])
        ruapavi = int(request.form['ruapavi'])
        moto = int(request.form['moto'])
        automovel = int(request.form['automovel'])
        total =  calculaCriterio(geladeira, banheiro, freezer, microondas, lavaloucas, maquinaroupa, secarroupas, empregado, computador, aguaencanada, ruapavi, moto, automovel)
        
        if nomeConvidado and sobrenomeConvidado and datanasc and rgConvidado and ufConvidado and cpfConvidado and enderecoConvidado and bairroConvidado and cidadeConvidado and cepConvidado and zonaConvidado and formacaoConvidado and escolaridadeConvidado and ano_escolaridade and periodoConvidado and estadoCivilConvidado and filhoConvidado and primeiroFilho and segundoFilho and nascimentoPrimeiroFilho and nascimentoSegundoFilho and trabalhoConvidado and horarioTrabalho and empresaConvidado and ramoConvidado and telefoneEmpresa and telefoneResidencial and celularConvidado and operadoraConvidado and opcaoOperadora and emailConvidado and pesquisaMercado and mktPubli and rjrTv and participouPesquisa and tipoPesquisa and dataUltimaPesquisa and assuntoUltimaPesquisa:    
            #revisar endereco e classificacao    
            convidado = Convidado(nome=nomeConvidado, sobrenome=sobrenomeConvidado, nascimento=datanasc, rg=rgConvidado, uf=ufConvidado, cpf=cpfConvidado, logradouro=enderecoConvidado, bairro=bairroConvidado, cidade=cidadeConvidado,cep=cepConvidado, zona=zonaConvidado, formacao=formacaoConvidado, instituicao=escolaridadeConvidado,semestre=ano_escolaridade, periodo=periodoConvidado, estado_civil=estadoCivilConvidado, filhos=filhoConvidado, filho_1=primeiroFilho, filho_2=segundoFilho, nascimento_primeiro_filho=nascimentoPrimeiroFilho, nascimento_segundo_filho=nascimentoSegundoFilho,possui_trabalho=trabalhoConvidado, periodo_trabalho=horarioTrabalho, empresa=empresaConvidado, ramo_empresa=ramoConvidado, telefone_empresa=telefoneEmpresa, telefone_residencial=telefoneResidencial, celular=celularConvidado, operadora=operadoraConvidado, plano_operadora=opcaoOperadora, email=emailConvidado, pesquisa_de_mercado=pesquisaMercado, ja_participou=participouPesquisa, tipo_pesquisa=tipoPesquisa, data_participacao=dataUltimaPesquisa, assunto=assuntoUltimaPesquisa, classificacao_socio=total, marketing_publicidade=mktPubli,radio_jornal_revista_tv=rjrTv )
            db.session.add(convidado)
            db.session.commit()
    
    
    return render_template('cadastro_convidado.html')


@app.route("/listar/convidado", methods=["GET","POST"])
def listarConvidado():
    convidados = Convidado.query.filter_by().all()

    if request.method == "POST":
        form = request.form("filtro_participou")
        convidados = Convidado.query.filter_by(ja_participou=form).all()

    return render_template('listar_convidado.html', convidados=convidados)


@app.route("/base")
def base():
    return render_template('base.html')


def handleId(id):
    empresa = id
    return empresa