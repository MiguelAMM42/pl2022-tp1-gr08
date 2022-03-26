import dominate
from dominate.tags import *
import unicodedata

#Code to generate HTML file for each athlete
def athletesGenerator(athletes):
    for a in athletes:
        doc = dominate.document(title=a['_id'])

        with doc:
            with div(id='header').add(ol()):
                p(a['nome_primeiro'] + ' ' + a['nome_ultimo'])
                p(a['modalidade'])

        fileName = "../out/athletes/" + a['_id'] + ".html"

        f = open(fileName, "w")
        f.write(doc.render())
        f.close()


#Dictionary of queries
queries_dict = {'A':'Datas extermas dos registos no dataset',
'B' : 'Distribuição por género em cada ano e no total',
'C' : 'Distribuição por modalidade em cada ano e no total',
'D' : 'Distribuição por idade e género (para a idade, considera apenas 2 escalões: < 35 anos e >= 35)',
'E' : 'Distribuição por morada',
'F' : 'Distribuição por estatuto de federado em cada ano',
'G' : 'Percentagem de aptos e não aptos por ano'}

#Code to generate the main page of the project
def htmlMAIN():
    
    doc = dominate.document(title='TP1_PL_EMD')

    with doc:
        with div(id='header').add(ol()):

            for i in queries_dict.keys():
                li(a(queries_dict[i].title(), href='../out/query%s/query%s.html' % (i, i) ))


    f = open("../out/index.html", "w")
    f.write(doc.render())
    f.close()


#(a) Datas externas dos registos no dataset --- HTML
def distByDatesHTML(dist):
    #HTML doc for each date
    for date in dist.keys():
        doc = dominate.document(title=date)

        with doc:
            with div(id='header').add(ol()):
                for athlete in dist[date]:
                    li(a(athlete['nome_primeiro'] + " " + athlete['nome_ultimo'], href='../../athletes/%s.html' % athlete['_id']))

        f = open("../out/queryA/dates/%s.html" % date, "w")
        f.write(doc.render())
        f.close()
    
    #main HTML doc of the query
    doc = dominate.document(title='Datas externas dos registos no dataset')

    with doc:
        with div(id='header').add(ol()):
            for date in dist.keys():
                li(a(date.title(), href='../queryA/dates/%s.html' % date))

    f = open("../out/queryA/queryA.html", "w")
    f.write(doc.render())
    f.close()

#(b) Distribuição por género em cada ano e no total --- HTML
def distByYearAndGenderHTML(dist):

    #HTML doc for each gender
    for gender in dist.keys():
        if gender == 'F':
            titleGender = 'feminino'
        else:
            titleGender = 'masculino' 
        doc = dominate.document(title=titleGender)

        with doc:
            with div(id='header').add(ol()):
                for year in dist[gender].keys():
                    li(a(year.title(), href='../queryA/%s/years/%s.html' % (genderTitle,year) ))

        f = open("../out/queryA/%s/%s.html" % (genderTitle,genderTitle), "w")
        f.write(doc.render())
        f.close()

    #main HTML doc of the query
    doc = dominate.document(title='Distribuição por género em cada ano e no total')

    with doc:
        with div(id='header').add(ol()):
            for gender in dist.keys():
                if gender == 'F':
                    titleGender = 'feminino'
                else:
                    titleGender = 'masculino' 
                li(a(genderTitle, href='../queryB/%s/%s.html' % (genderTitle,genderTitle)))

    f = open("../out/queryB/queryB.html", "w")
    f.write(doc.render())
    f.close()


#(e) Distribuição por morada --- HTML
def distByAddressHTML(dist):

    #HTML doc for each address
    for addr in dist.keys():
        doc = dominate.document(title=addr)

        with doc:
            with div(id='header').add(ol()):
                for athlete in dist[addr]:
                    li(a(athlete['nome_primeiro'] + " " + athlete['nome_ultimo'], href='../../athletes/%s.html' % athlete['_id']))

        f = open("../out/queryE/addresses/%s.html" % addr, "w")
        f.write(doc.render())
        f.close()
               
            

    #main HTML doc of the query
    doc = dominate.document(title='Distribuição por morada')

    with doc:
        with div(id='header').add(ol()):
            for addr in dist.keys():
                li(a(addr.title(), href='../queryE/addresses/%s.html' % addr))

    f = open("../out/queryE/queryE.html", "w")
    f.write(doc.render())
    f.close()
