import re


#FALTA ADICIONAR ESTATISTICAS
#DESTE MODO AS FUNÇOES IRÃO RETORNAR TUPLOS

#(a) Datas externas dos registos no dataset
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
    dist = {}
    for a in athletes:
        dataEMD = re.search(r'(\d{4})\-\d{2}\-\d{2}', a['dataEMD'])
        year = dataEMD.group(1)
        gender = a['genero']
        if year in dist:
            if gender in dist[year]:
                dist[year][gender].append(a)
            else:
                dist[year][gender] = [a]
        else:
            dist.update({year:{gender:[a]}})
            

    return dist


#(c) Distribuição por modalidade em cada ano e no total
def distByYearAndSport(athletes):
    dist = {}
    for a in athletes:
        dataEMD = re.search(r'(\d{4})\-\d{2}\-\d{2}', a['dataEMD'])
        year = dataEMD.group(1)
        sport = a['modalidade']
        if year in dist:
            if sport in dist[year]:
                dist[year][sport].append(a)
            else:
                dist[year][sport] = [a]
        else:
            dist.update({year:{sport:[a]}})

    return dist


#(d) Distribuição por idade e género (para a idade, considerar apenas 2 escalões: < 35 anos e >= 35)
def distByAgeAndGender(athletes):
    dist = {'menor35':{'F':[], 'M':[]}, 'maiorIgual35':{'F':[], 'M':[]}}
    for a in athletes:
        if int(a['idade']) < 35:
            if a['genero'] == 'F':
                dist['menor35']['F'].append(a)
            else:
                dist['menor35']['M'].append(a)
        else:
            if a['genero'] == 'F':
                dist['maiorIgual35']['F'].append(a)
            else:
                dist['maiorIgual35']['M'].append(a)

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
    dist = {}
    for a in athletes:
        dataEMD = re.search(r'(\d{4})\-\d{2}\-\d{2}', a['dataEMD'])
        year = dataEMD.group(1)
        federated = a['federado']
        if year in dist:
            if federated in dist[year]:
                dist[year][federated].append(a)
            else:
                dist[year][federated] = [a]
        else:
            dist.update({year:{federated:[a]}})

    return dist


#(g) Percentagem de aptos e não aptos por ano
def distByYearAndSuitable(athletes):
    dist = {}
    for a in athletes:
        dataEMD = re.search(r'(\d{4})\-\d{2}\-\d{2}', a['dataEMD'])
        year = dataEMD.group(1)
        suitable = a['resultado']
        if year in dist:
            if suitable in dist[year]:
                dist[year][suitable].append(a)
            else:
                dist[year][suitable] = [a]
        else:
            dist.update({year:{suitable:[a]}})

    return dist