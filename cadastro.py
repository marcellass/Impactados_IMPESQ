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
    genero = request.form['genero']
    faixaEtaria = request.form['faixaEtaria']
    classeEconomica = request.form['classeEconomica']
    if nomeEmpresa and cnpj and objetoPesquisa and tipoObjeto and horapesquisa and genero and faixaEtaria and classeEconomica:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into tbl_objeto_pesquisa (empresa_nome, cnpj, objeto_pesquisa, tipo_objeto, hora_pesquisa, genero, faixa_etaria, classe_economica) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (nomeEmpresa, cnpj, objetoPesquisa, tipoObjeto, horapesquisa, genero, faixaEtaria, classeEconomica))
        conn.commit()  

    return render_template('cadastro_pesquisa.html')

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



