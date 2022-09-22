import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from Entities import ObjetoPesquisaEntity

mysql = MySQL()
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
    faixaEtaria = request.form['idade']
    classeEconomica = request.form['classeEconomica']

    ObjetoPesquisaEntity.insert(nomeEmpresa, cnpj, objetoPesquisa, tipoObjeto, horapesquisa, faixaEtaria, classeEconomica)
    
    return render_template('cadastro_pesquisa.html')

@app.route('/listar', methods=['POST','GET'])
def listar():
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute('select user_name, user_cpf, user_endereco from tbl_user')
  data = cursor.fetchall()
  conn.commit()
  return render_template('listar.html', datas=data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8888))
    app.run(host='0.0.0.0', port=port)