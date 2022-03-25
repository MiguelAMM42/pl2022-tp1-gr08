import re


#FALTA ADICIONAR ESTATISTICAS
#DESTE MODO AS FUNÇOES IRÃO RETORNAR TUPLOS

#(a) Datas extermas dos registos no dataset
def distByDates(athletes):
    dist = {}
    for a in athletes:
        if a['dataEMD'] in dist:
            dist[a['dataEMD']].append(a)
        else:
            dist[a['dataEMD']] = [a]

    return dist


#(b) Distribuição por género em cada ano e no total
def distByYearAndGender(athletes):
    dist = {'F':{},'M':{}}
    for a in athletes:
        dataEMD = re.search(r'(\d{4})\-\d{2}\-\d{2}', a['dataEMD'])
        ano = dataEMD.group(1)
        if a['genero'] == 'F':
            if ano in dist['F']:
                dist['F'][ano].append(a)
            else:
                dist['F'][ano] = [a]
        else:
            if ano in dist['M']:
                dist['M'][ano].append(a)
            else:
                dist['M'][ano] = [a]

    return dist


#(c) Distribuição por modalidade em cada ano e no total
def distByYearAndSport(athletes):
    dist = {}
    for a in athletes:
        if a['morada'] in dist:
            dist[a['morada']].append(a)
        else:
            dist[a['morada']] = [a]

    return dist


#(d) Distribuição por idade e género (para a idade, considerar apenas 2 escalões: < 35 anos e >= 35)
def distByAgeAndGender(athletes):
    dist = {'F':{'menor35':[], 'maiorIgual35':[]}, 'M':{'menor35':[], 'maiorIgual35':[]}}
    for a in athletes:
        if a['genero'] == 'F':
            if int(a['idade']) < 35:
                dist['F']['menor35'].append(a)
            else:
                dist['F']['maiorIgual35'].append(a)
        else:
            if int(a['idade']) < 35:
                dist['M']['menor35'].append(a)
            else:
                dist['M']['maiorIgual35'].append(a)

    return dist


#(e) Distribuição por morada
def distByAddress(athletes):
    dist = {}
    for a in athletes:
        if a['morada'] in dist:
            dist[a['morada']].append(a)
        else:
            dist[a['morada']] = [a]

    return dist


#(f) Distribuição por estatuto de federado em cada ano
def distByYearAndFederated(athletes):
    dist = {'federado':{},'naoFederado':{}}
    for a in athletes:
        dataEMD = re.search(r'(\d{4})\-\d{2}\-\d{2}', a['dataEMD'])
        ano = dataEMD.group(1)
        if a['federado'] == 'true':
            if ano in dist['federado']:
                dist['federado'][ano].append(a)
            else:
                dist['federado'][ano] = [a]
        else:
            if ano in dist['naoFederado']:
                dist['naoFederado'][ano].append(a)
            else:
                dist['naoFederado'][ano] = [a]

    return dist


#(g) Percentagem de aptos e não aptos por ano
def distByYearAndSuitable(athletes):
    dist = {'apto':{},'naoApto':{}}
    for a in athletes:
        dataEMD = re.search(r'(\d{4})\-\d{2}\-\d{2}', a['dataEMD'])
        ano = dataEMD.group(1)
        if a['resultado'] == 'true':
            if ano in dist['apto']:
                dist['apto'][ano].append(a)
            else:
                dist['apto'][ano] = [a]
        else:
            if ano in dist['naoApto']:
                dist['naoApto'][ano].append(a)
            else:
                dist['naoApto'][ano] = [a]

    return dist