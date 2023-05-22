from app import app, db, loginManager
import os
from flask import render_template, flash, current_app, url_for, request, send_from_directory, jsonify, send_file
from app.models.RecrutadorEntity import Recutrador
from app.models.models.login import LoginForm
from app.models.models.cadastroRecrutador import CadastroRecrutadorForm
from app.models.EmpresaEntity import Empresa
from app.models.models.PesquisaModel import CadastroPesquisaModel
from app.models.PesquisaEntity import Pesquisa
from app.models.ConvidadoEntity import Convidado
from app.models.FormularioEntity import FormularioEntity
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas



@app.route('/cadastrar/formulario/<int:idEmpresa>/<int:idPesquisa>', methods=["GET", "POST"])
@app.route("/cadastrar/formulario/perguntas", methods=["POST"])
def novoFormulario(idEmpresa, idPesquisa):
    idEmpresa = idEmpresa
    idPesquisa = idPesquisa

    if request.method == 'POST':
        data = request.get_json()
        
        perguntas = data.get('perguntas', [])
        print(perguntas)
        for pergunta in perguntas:
            formulario = FormularioEntity(empresa_id=idEmpresa, pesquisa_id=idPesquisa, pergunta=pergunta)
            db.session.add(formulario)

        db.session.commit()


        return jsonify({'sucesso': 200})

    return render_template('cadastro_formulario.html')
    

@app.route('/conclusao/formulario/<int:idEmpresa>/<int:idPesquisa>', methods=["GET", "POST"])
def conclusaoFormulario(idEmpresa, idPesquisa):
    
    perguntas = FormularioEntity.query.filter_by(empresa_id=idEmpresa, pesquisa_id=idPesquisa).all()
    empresa = Empresa.query.filter_by(id=idEmpresa).first()
    pesquisa = Pesquisa.query.filter_by(id=idPesquisa).first()

    convidados = len(Convidado.query.filter_by(classificacao_socio=pesquisa.classeEconomica).all())
    
    return render_template('conclusao_formulario.html', perguntas=perguntas, idEmpresa=idEmpresa, idPesquisa=idPesquisa, empresa=empresa, pesquisa=pesquisa, convidados=convidados)


@app.route('/download/perguntas/<int:idEmpresa>/<int:idPesquisa>')
def downloadPerguntas(idEmpresa, idPesquisa):
    empresa = Empresa.query.filter_by(id=idEmpresa).first()
    pesquisa = Pesquisa.query.filter_by(id=idPesquisa).first()
    perguntas = FormularioEntity.query.filter_by(empresa_id=idEmpresa, pesquisa_id=idPesquisa).all()

    # Obter o diretório estático do Flask
    static_dir = current_app.static_folder

    # Criar o caminho completo para o arquivo PDF dentro do diretório estático
    pdf_path = os.path.join(static_dir, 'perguntas.pdf')

    # Criar o documento PDF
    c = canvas.Canvas(pdf_path, pagesize=A4)

    # Definir o cabeçalho
    c.setFont('Helvetica-Bold', 16)
    c.drawString(200, 800, '{}'.format(pesquisa.objetoPesquisa))
    c.setFont('Helvetica-Bold', 12)
    c.drawString(50, 750, 'Empresa: {}'.format(empresa.nome))
    c.drawString(200, 750, 'CNPJ: {}'.format(empresa.cnpj))


    c.setFont('Helvetica', 12)

    # Escrever as perguntas no arquivo PDF
    y = 700  # Posição vertical inicial
    numero_pergunta = 1
    for pergunta in perguntas:
        c.drawString(50, y, '{}. {}'.format(numero_pergunta, pergunta.pergunta))
        y -= 20  # Decrementar a posição vertical

        # Espaço para o usuário responder
        y -= 15
        c.drawString(50, y, 'Resposta: ________________________________________________')

        y -= 20  # Decrementar a posição vertical
        numero_pergunta += 1
        y -= 20  # Decrementar a posição vertical

    c.save()

    # Enviar o arquivo PDF como resposta para download
    return send_file(pdf_path, as_attachment=True)