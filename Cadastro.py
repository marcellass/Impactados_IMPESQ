import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from Entities import Objeto

mysql = MySQL()
objetoPesquisa = Objeto()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'impactados'
app.config['MYSQL_DATABASE_DB'] = 'pesquisa'
app.config['MYSQL_DATABASE_HOST'] = ''
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('cadastro_pesquisa.html')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastrar():
    nomeEmpresa = request.form['nomeEmpresa']
    cnpj = request.form['cnpj']
    objetoPesquisa = request.form['objetoPesquisa']
    tipoObjeto = request.form['tipoObjeto']
    horapesquisa = request.form['horapesquisa']
    idade = request.form['idade']
    classeEconomica = request.form['classeEconomica']

    objetoPesquisa.insert(nomeEmpresa, cnpj, objetoPesquisa, tipoObjeto, horapesquisa, idade, classeEconomica)
    
    return render_template('cadastro_pesquisa.html')

# @app.route('/gravar', methods=['POST','GET'])
# def gravar():
#   nome = request.form['nome']
#   cpf = request.form['cpf']
#   endereco = request.form['endereco']
#   if nome and email and senha:
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     cursor.execute('insert into tbl_user (user_name, user_cpf, user_endereco) VALUES (%s, %s, %s)', (nome, cpf, endereco))
#     conn.commit()
#   return render_template('mvc.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8888))
    app.run(host='0.0.0.0', port=port)