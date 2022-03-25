import dominate
from dominate.tags import *

queries_lst = ['Datas extermas dos registos no dataset',
'Distribuição por género em cada ano e no total',
'Distribuição por modalidade em cada ano e no total',
'Distribuição por idade e género (para a idade, considera apenas 2 escalões: < 35 anos e >= 35)',
'Distribuição por morada',
'Distribuição por estatuto de federado em cada ano',
'Percentagem de aptos e não aptos por ano']

def htmlMAIN():
    doc = dominate.document(title='TP1_PL_EMD')

    with doc:
        with div(id='header').add(ol()):
            for i in queries_lst:
                li(a(i.title(), href='../out/%s.html' % i))

    return doc


doc = htmlMAIN()
f = open("../out/index.html", "w")
f.write(doc.render())
f.close()



def distByAddressHTML(dist):
    doc = dominate.document(title='distByAddress')

    with doc:
        with div(id='header').add(ol()):
            for addr in dist.keys():
                li(a(addr.title(), href='../out/queryE/%s.html' % addr))

    return doc
