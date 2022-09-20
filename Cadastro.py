import os
from flask import Flask, request, abort , render_template


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('cadastro_pesquisa.html')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastrar():
    return render_template('cadastro_pesquisa.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)