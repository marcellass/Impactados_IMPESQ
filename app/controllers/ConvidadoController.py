from app import app, db, loginManager 
from flask import render_template, flash, redirect, url_for, request, send_from_directory
from app.models.ConvidadoEntity import Convidado
from app.controllers.utils.utils import calculaCriterio

@app.route("/listar/convidado", methods=["GET","POST"])
def listarConvidado():
    nome = request.args.get('nome')
    participacao = request.args.get('participacao')
    email = request.args.get('email')
    classe = request.args.get('classe')

    query = Convidado.query.filter_by()

    if nome:
        query = query.filter(Convidado.nome == nome)
    if participacao:
        if participacao == 'todos':
            query = Convidado.query.filter_by()
        else:
            query = query.filter(Convidado.ja_participou == participacao)
    if email:
        query = query.filter(Convidado.email == email)

    if classe:
        query = query.filter(Convidado.classificacao_socio == classe)

    convidados = query.all()
   

    return render_template('listar_convidado.html', convidados)



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
