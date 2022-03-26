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
#Está sorted por ano, genero e nome_primeiro
def distByYearAndGender(athletes):
    dist = {}
    distStats = {}
    womenCounter = 0
    menCounter = 0
    for a in athletes:
        dataEMD = re.search(r'(\d{4})\-\d{2}\-\d{2}', a['dataEMD'])
        year = dataEMD.group(1)
        gender = a['genero']
        if year in dist:
            if gender in dist[year]:
                dist[year][gender].append(a)
                distStats[year][gender] = distStats[year][gender] + 1
            else:
                dist[year][gender] = [a]
                distStats[year][gender] = 1
        else:
            dist.update({year:{gender:[a]}})
            distStats.update({year:{gender:1}})
            
    for year in distStats:
        if 'F' in distStats[year]:
            if 'M' in distStats[year]:
                womenCounter = womenCounter + distStats[year]['F']
                menCounter = menCounter + distStats[year]['M']
                total = distStats[year]['M'] + distStats[year]['F']
                distStats[year]['M'] = distStats[year]['M'] * 100 / total
                distStats[year]['F'] = 100.0 - distStats[year]['M']
            else:
                womenCounter = womenCounter + distStats[year]['F']
                distStats[year]['F'] = 100.0
                distStats[year]['M'] = 0
        else:
            menCounter = menCounter + distStats[year]['M']
            distStats[year]['M'] = 100
            distStats[year]['F'] = 0

    totaltotal = womenCounter + menCounter
    distStats.update({'total':{'F':womenCounter*100/totaltotal,'M':menCounter*100/totaltotal}})
    
    dist = distByYearAndGenderSorted(dist)

    return (dist,distStats)


def distByYearAndGenderSorted(dist):
    sorted_key_tuple = sorted(dist.items())
    sorted_dist = dict(sorted_key_tuple)
    
    for year in sorted_dist:
        sorted_gender_tuple = sorted(sorted_dist[year].items())
        sorted_dist[year] = dict(sorted_gender_tuple)
        for gender in sorted_dist[year]:
            sorted_dist[year][gender] = sorted(sorted_dist[year][gender], key = lambda i: i['nome_primeiro'])
    return sorted_dist



#(c) Distribuição por modalidade em cada ano e no total
#Sorted por ano, desporto e nome_primeiro
def distByYearAndSport(athletes):
    dist = {}
    distStats = {}
    distStats.update({'total':{}})
    for a in athletes:
        dataEMD = re.search(r'(\d{4})\-\d{2}\-\d{2}', a['dataEMD'])
        year = dataEMD.group(1)
        sport = a['modalidade']
        if year in dist:
            if sport in dist[year]:
                dist[year][sport].append(a)
                distStats[year][sport] = distStats[year][sport] + 1
            else:
                dist[year][sport] = [a]
                distStats[year][sport] = 1
        else:
            dist.update({year:{sport:[a]}})
            distStats.update({year:{sport:1}})

        if sport in distStats['total']:
            distStats['total'][sport] = distStats['total'][sport] + 1
        else:
            distStats['total'][sport] = 1

    for year in distStats:
        total = 0
        for sport in distStats[year]:
            total = total + distStats[year][sport]
        for sport in distStats[year]:
            distStats[year][sport] = distStats[year][sport] * 100 / total
            
    dist = distByYearAndSportSorted(dist)

    return (dist,distStats)


def distByYearAndSportSorted(dist):
    sorted_key_tuple = sorted(dist.items())
    sorted_dist = dict(sorted_key_tuple)
    
    for year in sorted_dist:
        sorted_gender_tuple = sorted(sorted_dist[year].items())
        sorted_dist[year] = dict(sorted_gender_tuple)
        for sport in sorted_dist[year]:
            sorted_dist[year][sport] = sorted(sorted_dist[year][sport], key = lambda i: i['nome_primeiro'])
    return sorted_dist
    


#(d) Distribuição por idade e género (para a idade, considerar apenas 2 escalões: < 35 anos e >= 35)
#Está sorted por nome_primeiro
def distByAgeAndGender(athletes):
    dist = {'menor35':{'F':[], 'M':[]}, 'maiorIgual35':{'F':[], 'M':[]}}
    distStats = {'menor35':{'F':0, 'M':0}, 'maiorIgual35':{'F':0, 'M':0}}
    womenCounter = 0
    menCounter = 0
    for a in athletes:
        if int(a['idade']) < 35:
            if a['genero'] == 'F':
                dist['menor35']['F'].append(a)
                distStats['menor35']['F'] = distStats['menor35']['F'] + 1
                womenCounter = womenCounter + 1
            else:
                dist['menor35']['M'].append(a)
                distStats['menor35']['M'] = distStats['menor35']['M'] + 1
                menCounter = menCounter + 1
        else:
            if a['genero'] == 'F':
                dist['maiorIgual35']['F'].append(a)
                distStats['maiorIgual35']['F'] = distStats['maiorIgual35']['F'] + 1
                womenCounter = womenCounter + 1
            else:
                dist['maiorIgual35']['M'].append(a)
                distStats['maiorIgual35']['M'] = distStats['maiorIgual35']['M'] + 1
                menCounter = menCounter + 1

    distStats['menor35']['F'] = distStats['menor35']['F'] * 100 / (distStats['menor35']['F'] + distStats['menor35']['M'])
    distStats['menor35']['M'] = 100 - distStats['menor35']['F']
    distStats['maiorIgual35']['F'] = distStats['maiorIgual35']['F'] * 100 / (distStats['maiorIgual35']['F'] + distStats['maiorIgual35']['M'])
    distStats['maiorIgual35']['M'] = 100 - distStats['maiorIgual35']['F']
    
    dist = distByAgeAndGenderSorted(dist)

    return (dist,distStats)

def distByAgeAndGenderSorted(dist):  
    for age in dist:
        for gender in dist[age]:
            dist[age][gender] = sorted(dist[age][gender], key = lambda i: i['nome_primeiro'])
    return dist
    


#(e) Distribuição por morada
#sorted por morada e nome
def distByAddress(athletes):
    dist = {}
    for a in athletes:
        if a['morada'] in dist:
            dist[a['morada']].append(a)
        else:
            dist[a['morada']] = [a]
        
    dist = distByAdressSorted(dist)

    return dist

def distByAdressSorted(dist):
    sorted_key_tuple = sorted(dist.items())
    sorted_dist = dict(sorted_key_tuple)
    
    for adress in sorted_dist:
        sorted_dist[adress] = sorted(sorted_dist[adress], key = lambda i: i['nome_primeiro'])
        #print(sorted(sorted_dist[adress], key = lambda i: i['index']))
    return sorted_dist
    


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