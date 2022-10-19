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
def main():
    return render_template('cadastro_pesquisa.html')

@app.route('/cadastrar', methods=['POST', 'GET'])
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

@app.route('/convidado', methods=['POST','GET'])
def cadastro_convidado():
    nomeConvidado = request.form['nomeConvidado']
    sobrenomeConvidado = request.form['sobrenomeConvidado']
    datanasc = request.form['datanasc']
    rgConvidado = request.form['rgConvidado']
    ufConvidado = request.form['ufConvidado'] #VER DEPOIS
    cpfConvidado = request.form['cpfConvidado']
    enderecoConvidado = request.form['enderecoConvidado']
    bairroConvidado = request.form['bairroConvidado']
    cidadeConvidado = request.form['cidadeConvidado']
    cepConvidado = request.form['cepConvidado']
    if nomeConvidado and sobrenomeConvidado and datanasc and rgConvidado and ufConvidado and cpfConvidado and enderecoConvidado and bairroConvidado and cidadeConvidado and cepConvidado:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into tbl_cadastro_convidado (nomeConvidado, sobrenomeConvidado, datanasc, rgConvidado, ufConvidado, cpfConvidado, enderecoConvidado, bairroConvidado, cidadeConvidado, cepConvidado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (nomeConvidado, sobrenomeConvidado, datanasc, rgConvidado, ufConvidado, cpfConvidado, enderecoConvidado, bairroConvidado, cidadeConvidado, cepConvidado))
        conn.commit()

    return render_template('cadastro_convidado.html')

@app.route('/listar2', methods=['POST','GET'])
def listar_convidado():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select nomeConvidado, sobrenomeConvidado, datanasc, rgConvidado, ufConvidado, cpfConvidado, enderecoConvidado, bairroConvidado, cidadeConvidado, cepConvidado')
    data = cursor.fetchall()
    conn.commit()
    return render_template('listar_convidado.html', datas=data)

    

@app.route('/listar', methods=['POST','GET'])
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



