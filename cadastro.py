import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'impactados'
app.config['MYSQL_DATABASE_DB'] = 'pesquisa'
app.config['MYSQL_DATABASE_HOST'] = 'db'
mysql.init_app(app)

@app.route('/')
def main_pesquisa():
    return render_template('cadastro_pesquisa.html')

@app.route('/convidado')
def main_convidado():
    return render_template('cadastro_convidado.html')

@app.route('/cadastrar/pesquisa', methods=['POST','GET'])
def cadastrar():
    nomeEmpresa = request.form['nomeEmpresa']
    cnpj = request.form['cnpj']
    objetoPesquisa = request.form['objetoPesquisa']
    tipoObjeto = request.form['tipoObjeto']
    horapesquisa = str(request.form['horapesquisa'])
    genero2 = request.form.getlist('genero')
    genero =' '.join(map(str,genero2))
    faixaEtaria = request.form['faixaEtaria']
    classeEconomica2 = request.form.getlist('classeEconomica')
    classeEconomica =' '.join(map(str,classeEconomica2))
    if nomeEmpresa and cnpj and objetoPesquisa and tipoObjeto and horapesquisa and genero and faixaEtaria and classeEconomica:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into tbl_objeto_pesquisa (empresa_nome, cnpj, objeto_pesquisa, tipo_objeto, hora_pesquisa, genero, faixa_etaria, classe_economica) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (nomeEmpresa, cnpj, objetoPesquisa, tipoObjeto, horapesquisa, genero, faixaEtaria, classeEconomica))
        conn.commit()  

    return render_template('cadastro_pesquisa.html')

@app.route('/cadastrar/convidado', methods=['POST', 'GET'])
def convidado():
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
    if nomeConvidado and sobrenomeConvidado and datanasc and rgConvidado and ufConvidado and cpfConvidado and enderecoConvidado and bairroConvidado and cidadeConvidado and cepConvidado and zonaConvidado and formacaoConvidado and escolaridadeConvidado and ano_escolaridade and periodoConvidado and estadoCivilConvidado and filhoConvidado and primeiroFilho and segundoFilho and nascimentoPrimeiroFilho and nascimentoSegundoFilho and trabalhoConvidado and horarioTrabalho and empresaConvidado and ramoConvidado and telefoneEmpresa and telefoneResidencial and celularConvidado and operadoraConvidado and opcaoOperadora and emailConvidado and pesquisaMercado and mktPubli and rjrTv and participouPesquisa and tipoPesquisa and dataUltimaPesquisa and assuntoUltimaPesquisa:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into tbl_cadastro_convidado (nomeConvidado, sobrenomeConvidado, datanasc, rgConvidado, ufConvidado, cpfConvidado, enderecoConvidado, bairroConvidado, cidadeConvidado, cepConvidado, zonaConvidado, formacaoConvidado, escolaridadeConvidado, ano_escolaridade, periodoConvidado, estadoCivilConvidado, filhoConvidado, primeiroFilho, segundoFilho, nascimentoPrimeiroFilho, nascimentoSegundoFilho, trabalhoConvidado, horarioTrabalho, empresaConvidado, ramoConvidado, telefoneEmpresa, telefoneResidencial, celularConvidado, operadoraConvidado, opcaoOperadora, emailConvidado, pesquisaMercado, mktPubli, rjrTv, participouPesquisa, tipoPesquisa, dataUltimaPesquisa, assuntoUltimaPesquisa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (nomeConvidado, sobrenomeConvidado, datanasc, rgConvidado, ufConvidado, cpfConvidado, enderecoConvidado, bairroConvidado, cidadeConvidado, cepConvidado, zonaConvidado, formacaoConvidado, escolaridadeConvidado, ano_escolaridade, periodoConvidado, estadoCivilConvidado, filhoConvidado, primeiroFilho, segundoFilho, nascimentoPrimeiroFilho, nascimentoSegundoFilho, trabalhoConvidado, horarioTrabalho, empresaConvidado, ramoConvidado, telefoneEmpresa, telefoneResidencial, celularConvidado, operadoraConvidado, opcaoOperadora, emailConvidado, pesquisaMercado, mktPubli, rjrTv, participouPesquisa, tipoPesquisa, dataUltimaPesquisa, assuntoUltimaPesquisa ))
        conn.commit()

    return render_template('cadastro_convidado.html')

@app.route('/listar/convidado', methods=['POST','GET'])
def listar_convidado():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select * from tbl_cadastro_convidado')
    data = cursor.fetchall()
    conn.commit()
    return render_template('listar_convidado.html', datas=data)

    

@app.route('/listar/pesquisa', methods=['POST','GET'])
def listar():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select empresa_nome, cnpj, objeto_pesquisa, tipo_objeto, hora_pesquisa, genero, faixa_etaria, classe_economica from tbl_objeto_pesquisa')
    data = cursor.fetchall()
    conn.commit()
    return render_template('listar_pesquisa.html', datas=data)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8888))
    app.run(host='0.0.0.0', port=port)



