def calculaCriterioGeladeira(geladeira):
    pontuacao = geladeira
    if geladeira == 1:
        pontuacao = 3
    elif geladeira == 2:
         pontuacao = 7
    elif geladeira == 3:
         pontuacao = 10
    elif geladeira == 4:
     pontuacao = 14
    else:
         geladeira == 0
    return pontuacao

def defineClassificacao(total):
    classificacao = ""
    if total >= 1:
        classificacao = "A"
        return classificacao


def calculaCriterio(geladeira): 
    geladeira  = calculaCriterioGeladeira(geladeira)
    total = geladeira #soma
    classificacaoSocial = defineClassificacao(total)
    return classificacaoSocial
