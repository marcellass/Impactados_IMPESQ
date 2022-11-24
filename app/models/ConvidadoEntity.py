from app import db


class Convidado(db.Model):
    __tablename__ = "tbl_convidados"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120))
    sobrenome = db.Column(db.String)
    nascimento = db.Column(db.String)
    cpf = db.Column(db.String)
    rg = db.Column(db.String)
    uf = db.Column(db.String)


    #formacao
    formacao = db.Column(db.String)
    instituicao = db.Column(db.String)
    semestre = db.Column(db.String)
    periodo = db.Column(db.String)

    #familia
    estado_civil = db.Column(db.String)
    filhos = db.Column(db.String)
    filho_1 = db.Column(db.String)
    nascimento_primeiro_filho = db.Column(db.String)
    filho_2 = db.Column(db.String)
    nascimento_segundo_filho = db.Column(db.String)


    #Trabalho
    possui_trabalho = db.Column(db.String)
    periodo_trabalho = db.Column(db.String)
    empresa = db.Column(db.String)
    ramo_empresa = db.Column(db.String)
    telefone_empresa = db.Column(db.String)


    #contato
    telefone_residencial = db.Column(db.String)
    celular = db.Column(db.String)
    operadora = db.Column(db.String)
    plano_operadora = db.Column(db.String)
    email = db.Column(db.String)

    #historico participacao
    pesquisa_de_mercado = db.Column(db.String)
    marketing_publicidade = db.Column(db.String)
    radio_jornal_revista_tv = db.Column(db.String)
    ja_participou = db.Column(db.String)
    tipo_pesquisa = db.Column(db.String)
    data_participacao = db.Column(db.String)
    assunto = db.Column(db.String)


    #endereco
    logradouro = db.Column(db.String(120))
    cep = db.Column(db.String)
    bairro= db.Column(db.String)
    cidade = db.Column(db.String)
    zona = db.Column(db.String)


    #classificacao
    classificacao_socio = db.Column(db.String)



    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

        # contrutor da classe
    def __init__(self, nome, sobrenome, email, nascimento, cpf, rg, uf, formacao, instituicao, semestre, periodo,estado_civil, filhos, filho_1, filho_2, possui_trabalho, periodo_trabalho, empresa, ramo_empresa, telefone_empresa, telefone_residencial, celular, operadora, plano_operadora, pesquisa_de_mercado, marketing_publicidade, radio_jornal_revista_tv, ja_participou, tipo_pesquisa, data_participacao, assunto, classificacao_socio,  logradouro, cep, bairro, cidade, zona, nascimento_primeiro_filho, nascimento_segundo_filho):
        

        self.nascimento_primeiro_filho = nascimento_primeiro_filho
        self.nascimento_segundo_filho = nascimento_segundo_filho
        self.estado_civil = estado_civil
        self.possui_trabalho = possui_trabalho
        self.periodo_trabalho = periodo_trabalho
        self.empresa = empresa 
        self.ramo_empresa = ramo_empresa
        self.telefone_empresa = telefone_empresa
        self.telefone_residencial = telefone_residencial
        self.operadora =operadora
        self.plano_operadora = plano_operadora
        self.pesquisa_de_mercado = pesquisa_de_mercado
        self.marketing_publicidade = marketing_publicidade
        self.radio_jornal_revista_tv = radio_jornal_revista_tv
        self.tipo_pesquisa = tipo_pesquisa
        self.data_participacao = data_participacao
        self.classificacao_socio =classificacao_socio
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.nascimento = nascimento
        self.cpf = cpf
        self.rg = rg
        self.uf = uf
        self.semestre =semestre
        self.ja_participou = ja_participou
        self.assunto = assunto
        self.celular = celular
        self.formacao = formacao 
        self.periodo = periodo
        self.filhos = filhos
        self.filho_1 = filho_1
        self.filho_2 = filho_2
        self.instituicao = instituicao
        self.logradouro = logradouro
        self.cep = cep 
        self.bairro = bairro
        self.cidade = cidade 
        self.zona = zona


    # representacao
    # como a classe apresenta os registros
    def __repr__(self):


        convidado = [self.estado_civil, 
        self.possui_trabalho,
        self.periodo_trabalho,
        self.empresa,
        self.ramo_empresa,
        self.telefone_empresa,
        self.telefone_residencial,
        self.operadora,
        self.plano_operadora,
        self.pesquisa_de_mercado,
        self.marketing_publicidade,
        self.radio_jornal_revista_tv,
        self.tipo_pesquisa,
        self.data_participacao, 
        self.classificacao_socio, 
        self.id, 
        self.nome,
        self.sobrenome, 
        self.email,
        self.nascimento,
        self.cpf,
        self.rg,
        self.uf,
        self.semestre,
        self.ja_participou, 
        self.assunto,
        self.celular, 
        self.formacao, 
        self.periodo,
        self.filhos,
        self.filho_1,
        self.filho_2,
        self.instituicao,
        self.logradouro, 
        self.cep, 
        self.bairro,
        self.cidade, 
        self.zona, 
        self.nascimento_segundo_filho,
        self.nascimento_primeiro_filho ]

        return "<%r>" % convidado

