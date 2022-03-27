import sys
import re
import unicodedata

def reader(fileName):

    f=open(fileName)

    header = f.readline()[:-1]
    params = header.split(",")

    #criação do dicionário para alocação das estruturas
    dic = dict()
    iterator = 0
    for param in params:
        param = unicodedata.normalize('NFD', param).encode('ascii', 'ignore').decode("utf-8")
        if("/" in param):
            param = param.replace("/","_")
        dic[param] = []

    parser = r'(?P<_id>[A-Za-z0-9_À-ÿ]{24}),(?P<index>\d+),(?P<dataEMD>\d{4}-\d{2}-\d{2}),(?P<nome_primeiro>[A-Za-zÀ-ÿ]+),(?P<nome_ultimo>[A-Za-zÀ-ÿ]+),(?P<idade>\d+),(?P<genero>[Ff]|[Mm]),(?P<morada>[A-Za-zÀ-ÿ]+),(?P<modalidade>[A-Za-zÀ-ÿ]+),(?P<clube>[A-Za-zÀ-ÿ]+),(?P<email>(\w+[\.]?\w+)+@(\w+\-?\w+\.)+(\w+\-?\w+)+),(?P<federado>[Tt][Rr][Uu][Ee]|[Ff][Aa][Ll][Ss][Ee]),(?P<resultado>[Tt][Rr][Uu][Ee]|[Ff][Aa][Ll][Ss][Ee])'
    pparser = re.compile(parser)

    dic_keys = list(dic.keys())

    for line in f:
        register = pparser.search(line)
        if register:
            #print(register.groups())
            d = register.groupdict()
            ##print(d)
            i = 0
            for i in range(len(params)):
                dic[dic_keys[i]].append(d[dic_keys[i]])
                i = i + 1

    lstAthletes = [dict(zip(dic,t)) for t in zip(*dic.values())]

    return(lstAthletes)



