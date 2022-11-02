def calculaCriterioGeladeira(geladeira):
    pontuacao = geladeira
    if geladeira == 1:
        pontuacao = 2
    elif geladeira == 2:
         pontuacao = 3
    elif geladeira == 3:
         pontuacao = 5
    elif geladeira == 4:
     pontuacao = 5
    else:
         geladeira == 0
    return pontuacao


def calculaCriterioBanheiro(banheiro):
    pontuacao = banheiro
    if banheiro == 1:
        pontuacao = 3
    elif banheiro == 2:
         pontuacao = 7
    elif banheiro == 3:
         pontuacao = 10
    elif banheiro == 4:
     pontuacao = 14
    else:
         banheiro == 0
    return pontuacao

def calculaCriterioFreezer(freezer):
    pontuacao = freezer
    if freezer == 1:
        pontuacao = 2
    elif freezer == 2:
         pontuacao = 4
    elif freezer == 3:
         pontuacao = 6
    elif freezer == 4:
     pontuacao = 6
    else:
         freezer == 0
    return pontuacao

def calculaCriterioMicroOndas(microOndas):
    pontuacao = microOndas
    if microOndas == 1:
        pontuacao = 2
    elif microOndas == 2:
         pontuacao = 4
    elif microOndas == 3:
         pontuacao = 4
    elif microOndas == 4:
     pontuacao = 4
    else:
         microOndas == 0
    return pontuacao

def calculaCriterioLavaLoucas(lavaLoucas):
    pontuacao = lavaLoucas
    if lavaLoucas == 1:
        pontuacao = 3
    elif lavaLoucas == 2:
         pontuacao = 6
    elif lavaLoucas == 3:
         pontuacao = 6
    elif lavaLoucas == 4:
     pontuacao = 6
    else:
         lavaLoucas == 0
    return pontuacao

def calculaCriterioLavaRoupa(lavaRoupas):
    pontuacao = lavaRoupas
    if lavaRoupas == 1:
        pontuacao = 2
    elif lavaRoupas == 2:
         pontuacao = 4
    elif lavaRoupas == 3:
         pontuacao = 6
    elif lavaRoupas == 4:
        pontuacao = 6
    else:
         lavaRoupas == 0
    return pontuacao

def calculaCriterioSecaRoupa(secaRoupa):
    pontuacao = secaRoupa
    if secaRoupa == 1:
        pontuacao = 2
    elif secaRoupa == 2:
         pontuacao = 2
    elif secaRoupa == 3:
         pontuacao = 2
    elif secaRoupa == 4:
        pontuacao = 2
    else:
         secaRoupa == 0
    return pontuacao

##EMPREGADOS MENSALISTAS 0 3 7 10 13

def calculaCriterioEmpregado(empregado):
    pontuacao = empregado
    if empregado == 1:
        pontuacao = 3
    elif empregado == 2:
         pontuacao = 7
    elif empregado == 3:
         pontuacao = 10
    elif empregado == 4:
        pontuacao = 13
    else:
         empregado == 0
    return pontuacao
##MICROCOMPUTADOR
def calculaCriterioComputador(computador):
    pontuacao = computador
    if computador == 1:
        pontuacao = 3
    elif computador == 2:
         pontuacao = 6
    elif computador == 3:
         pontuacao = 18
    elif computador == 4:
        pontuacao = 11
    else:
         computador == 0
    return pontuacao

##Agua Encanada
def calculaCriterioAguaEncanada(aguaEncanada):
    pontuacao = aguaEncanada
    if aguaEncanada == 1:
        pontuacao = 4
    else:
         aguaEncanada == 0
    return pontuacao

def calculaCriterioRuaPavimentada(ruaPavimentada):
    pontuacao = ruaPavimentada
    if ruaPavimentada == 1:
        pontuacao = 2
    else:
         ruaPavimentada == 0
    return pontuacao

def calculaCriterioMotocicleta(motocicleta):
    pontuacao = motocicleta
    if motocicleta == 1:
        pontuacao = 1
    elif motocicleta == 2:
         pontuacao = 3
    elif motocicleta == 3:
         pontuacao = 3
    elif motocicleta == 4:
        pontuacao = 3
    else:
         motocicleta == 0
    return pontuacao
    
def calculaCriterioAutomovel(automovel):
    pontuacao = automovel
    if automovel == 1:
        pontuacao = 3
    elif automovel == 2:
         pontuacao = 5
    elif automovel == 3:
         pontuacao = 8
    elif automovel == 4:
        pontuacao = 11
    else:
         automovel == 0
    return pontuacao


def defineClassificacao(pontuacaoTotal):
    classificacao = ""
    if pontuacaoTotal >= 45:
        classificacao = "A"
    elif pontuacaoTotal >= 38 and pontuacaoTotal <= 44:
        classificacao = "B1"
    elif pontuacaoTotal >= 29 and pontuacaoTotal <= 37:
        classificacao = "B2"
    elif pontuacaoTotal >= 23 and pontuacaoTotal <= 28:
        classificacao = "C1"
    elif pontuacaoTotal >= 17 and pontuacaoTotal <= 22:
        classificacao = "C2"
    elif pontuacaoTotal >= 0 and pontuacaoTotal <= 16:
        classificacao = "DE"
    return classificacao


def calculaCriterio(geladeira, banheiro, freezer, microOndas, lavaLoucas, lavaRoupa, secaRoupa, empregado, computador, aguaEncanada, ruaPavimentada, motocicleta, automovel): 
    geladeira  = calculaCriterioGeladeira(geladeira)
    banheiro = calculaCriterioBanheiro(banheiro)
    freezer = calculaCriterioFreezer(freezer)
    microOndas = calculaCriterioMicroOndas(microOndas)
    lavaLoucas = calculaCriterioLavaLoucas(lavaLoucas)
    lavaRoupa = calculaCriterioLavaRoupa(lavaRoupa)
    secaRoupa = calculaCriterioSecaRoupa(secaRoupa)
    empregado = calculaCriterioEmpregado(empregado)
    computador = calculaCriterioComputador(computador)
    aguaEncanada = calculaCriterioAguaEncanada(aguaEncanada)
    ruaPavimentada = calculaCriterioRuaPavimentada(ruaPavimentada)
    motocicleta = calculaCriterioMotocicleta(motocicleta)
    automovel = calculaCriterioAutomovel(automovel)

    total = geladeira + banheiro + freezer + microOndas + lavaLoucas + lavaRoupa + secaRoupa + empregado + computador + aguaEncanada + ruaPavimentada + motocicleta + automovel

    classificacaoSocial = defineClassificacao(total)

    return classificacaoSocial
