from app import app, db, loginManager 
from flask import render_template, make_response, jsonify

@app.route('/react', methods=['GET'])
def index():

    nome = "felipe"
    sobrenome = "pereira"

    datas = jsonify({'nome': nome, 'sobrenome': sobrenome})
    
    return render_template('index.html', nome=nome, sobrenome=sobrenome)