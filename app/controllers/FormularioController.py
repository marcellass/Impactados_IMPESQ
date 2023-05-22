from app import app, db, loginManager
import os
from flask import render_template, flash, current_app, url_for, request, send_from_directory, jsonify, send_file,redirect
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


@app.route("/formulario/elegibilidade/edicao", methods=["GET","POST"])
def elegibilidadeEdicao():
    idPesquisa = request.form['id']

    queryPesquisa = Pesquisa.query.filter_by(id=idPesquisa).first()
    queryFormulario = FormularioEntity.query.filter_by(pesquisa_id=idPesquisa).all()
    lenFormulario = len(queryFormulario)

    print(queryPesquisa)

    if (lenFormulario == 0):
        return redirect(url_for('novoFormulario', idEmpresa = queryPesquisa.idEmpresa , idPesquisa=idPesquisa))
    else:
        return redirect(url_for('conclusaoFormulario', idEmpresa = queryPesquisa.idEmpresa , idPesquisa=idPesquisa))
    


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

    static_dir = current_app.static_folder

    pdf_path = os.path.join(static_dir, 'perguntas.pdf')

    # Criar o documento PDF
    c = canvas.Canvas(pdf_path, pagesize=A4)

    
    c.setFont('Helvetica-Bold', 16)
    c.drawString(250, 800, '{}'.format("IMPESQ"))
    c.setFont('Helvetica-Bold', 12)
    c.drawString(175, 780, '{}'.format("Transformando Opiniões em Dados"))
    
    c.setFont('Helvetica', 11)
    c.drawString(50, 730, 'Empresa: {}'.format(empresa.nome))
    c.drawString(380, 730, 'CNPJ: {}'.format(empresa.cnpj))
    c.drawString(50, 700, 'Classificação : {}'.format(pesquisa.classeEconomica))
    c.drawString(380, 700, 'Faixa etária: {}'.format(pesquisa.faixaEtaria))


    c.setFont('Helvetica-Bold', 11)
    c.drawString(50, 660, '{}'.format("Responda as seguintes questões sobre o objeto em pesquisa: {}.".format(pesquisa.objetoPesquisa)))

    c.setFont('Helvetica', 11)

    # Escrever as perguntas no arquivo PDF
    y = 630  # Posição vertical inicial
    numero_pergunta = 1
    for pergunta in perguntas:
        c.drawString(50, y, '{}. {}'.format(numero_pergunta, pergunta.pergunta))
        y -= 20  # Decrementar a posição vertical

        # Espaço para o usuário responder
        y -= 15
        c.drawString(50, y, 'Resposta: __________________________________________________________________________')

        y -= 20  # Decrementar a posição vertical
        numero_pergunta += 1
        y -= 20  # Decrementar a posição vertical

    c.save()

    # Enviar o arquivo PDF como resposta para download
    return send_file(pdf_path, as_attachment=True)