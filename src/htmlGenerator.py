import dominate
from dominate.tags import *
from queries import *
import unicodedata
import os

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
    #Code to generate a folder for each year
    for year in dist.keys():
        yearPath = '../out/queryB/' + year
        if not os.path.exists(yearPath):
            os.makedirs(yearPath)

    
    #Code to generate HTML doc for each gender in each year
    for year in dist.keys():
        for gender in dist[year].keys():
            if gender == 'F':
                genderTitle = 'feminino'
            else:
                genderTitle = 'masculino'
            doc = dominate.document(title=gender)

            with doc:
                with div(id='header').add(ol()):
                    for athlete in dist[year][gender]:
                        li(a(athlete['nome_primeiro'] + " " + athlete['nome_ultimo'], href='../../athletes/%s.html' % athlete['_id']))

            f = open("../out/queryB/%s/%s.html" % (year,genderTitle), "w")
            f.write(doc.render())
            f.close()
            
        

    #Code to generate HTML doc for each year
    for year in dist.keys():

        doc = dominate.document(title=year)

        with doc:
            with div(id='header').add(ol()):
                for gender in dist[year].keys():
                    if gender == 'F':
                        genderTitle = 'feminino'
                    else:
                        genderTitle = 'masculino'
                    li(a(genderTitle, href='../%s/%s.html' % (year,genderTitle) ))

        f = open("../out/queryB/%s/%s.html" % (year,year), "w")
        f.write(doc.render())
        f.close()

    
    #main HTML doc of the query
    doc = dominate.document(title='Distribuição por género em cada ano e no total')

    with doc:
        with div(id='header').add(ol()):
            for year in dist.keys():
                li(a(year, href='../queryB/%s/%s.html' % (year,year)))

    f = open("../out/queryB/queryB.html", "w")
    f.write(doc.render())
    f.close()



#(c) Distribuição por modalidade em cada ano e no total --- HTML
def distByYearAndSportHTML(dist):
    #Code to generate a folder for each year
    for year in dist.keys():
        yearPath = '../out/queryC/' + year
        if not os.path.exists(yearPath):
            os.makedirs(yearPath)

    
    #Code to generate HTML doc for each sport in each year
    for year in dist.keys():
        for sport in dist[year].keys():
            doc = dominate.document(title=sport)

            with doc:
                with div(id='header').add(ol()):
                    for athlete in dist[year][sport]:
                        li(a(athlete['nome_primeiro'] + " " + athlete['nome_ultimo'], href='../../athletes/%s.html' % athlete['_id']))

            f = open("../out/queryC/%s/%s.html" % (year, sport), "w")
            f.write(doc.render())
            f.close()
            
        

    #Code to generate HTML doc for each year
    for year in dist.keys():

        doc = dominate.document(title=year)

        with doc:
            with div(id='header').add(ol()):
                for sport in dist[year].keys():
                    li(a(sport, href='../%s/%s.html' % (year,sport) ))

        f = open("../out/queryC/%s/%s.html" % (year,year), "w")
        f.write(doc.render())
        f.close()

    
    #main HTML doc of the query
    doc = dominate.document(title='Distribuição por modalidade em cada ano e no total')

    with doc:
        with div(id='header').add(ol()):
            for year in dist.keys():
                li(a(year, href='../queryC/%s/%s.html' % (year,year)))

    f = open("../out/queryC/queryC.html", "w")
    f.write(doc.render())
    f.close()


#(d) Distribuição por idade e género (para a idade, considerar apenas 2 escalões: < 35 anos e >= 35) --- HTML
def distByAgeAndGenderHTML(dist):
    #Code to generate a folder for each age interval
    for age in dist.keys():
        agePath = '../out/queryD/' + age
        if not os.path.exists(agePath):
            os.makedirs(agePath)

    
    #Code to generate HTML doc for each gender in each age interval
    for age in dist.keys():
        for gender in dist[age].keys():
            doc = dominate.document(title=gender)

            with doc:
                with div(id='header').add(ol()):
                    for athlete in dist[age][gender]:
                        li(a(athlete['nome_primeiro'] + " " + athlete['nome_ultimo'], href='../../athletes/%s.html' % athlete['_id']))

            f = open("../out/queryD/%s/%s.html" % (age, gender), "w")
            f.write(doc.render())
            f.close()
            
        

    #Code to generate HTML doc for each year
    for age in dist.keys():

        doc = dominate.document(title=age)

        with doc:
            with div(id='header').add(ol()):
                for gender in dist[age].keys():
                    li(a(gender, href='../%s/%s.html' % (age,gender) ))

        f = open("../out/queryD/%s/%s.html" % (age,age), "w")
        f.write(doc.render())
        f.close()

    
    #main HTML doc of the query
    doc = dominate.document(title='Distribuição por idade e género')

    with doc:
        with div(id='header').add(ol()):
            for year in dist.keys():
                li(a(year, href='../queryD/%s/%s.html' % (year,year)))

    f = open("../out/queryD/queryD.html", "w")
    f.write(doc.render())
    f.close()


#(e) Distribuição por morada --- HTML
def distByAddressHTML(dist):
    #Code to generate a folder dor the addresses
    addrPath = '../out/queryE/addresses'
    if not os.path.exists(addrPath):
        os.makedirs(addrPath)

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


#(f) Distribuição por estatuto de federado em cada ano --- HTML
def distByYearAndFederatedHTML(dist):
    #Code to generate a folder for each year
    for year in dist.keys():
        yearPath = '../out/queryF/' + year
        if not os.path.exists(yearPath):
            os.makedirs(yearPath)

    
    #Code to generate HTML doc for each state in each year
    for year in dist.keys():
        for federated in dist[year].keys():
            doc = dominate.document(title=federated)

            with doc:
                with div(id='header').add(ol()):
                    for athlete in dist[year][federated]:
                        li(a(athlete['nome_primeiro'] + " " + athlete['nome_ultimo'], href='../../athletes/%s.html' % athlete['_id']))

            f = open("../out/queryF/%s/%s.html" % (year, federated), "w")
            f.write(doc.render())
            f.close()
            
        

    #Code to generate HTML doc for each year
    for year in dist.keys():

        doc = dominate.document(title=year)

        with doc:
            with div(id='header').add(ol()):
                for federated in dist[year].keys():
                    li(a(federated, href='../%s/%s.html' % (year,federated) ))

        f = open("../out/queryF/%s/%s.html" % (year,year), "w")
        f.write(doc.render())
        f.close()

    
    #main HTML doc of the query
    doc = dominate.document(title='Distribuição por estatuto de federado em cada ano')

    with doc:
        with div(id='header').add(ol()):
            for year in dist.keys():
                li(a(year, href='../queryF/%s/%s.html' % (year,year)))

    f = open("../out/queryF/queryF.html", "w")
    f.write(doc.render())
    f.close()



#(g) Percentagem de aptos e não aptos por ano --- HTML
def distByYearAndSuitableHTML(dist):
    #Code to generate a folder for each year
    for year in dist.keys():
        yearPath = '../out/queryG/' + year
        if not os.path.exists(yearPath):
            os.makedirs(yearPath)

    
    #Code to generate HTML doc for each result in each year
    for year in dist.keys():
        for suitable in dist[year].keys():
            doc = dominate.document(title=suitable)

            with doc:
                with div(id='header').add(ol()):
                    for athlete in dist[year][suitable]:
                        li(a(athlete['nome_primeiro'] + " " + athlete['nome_ultimo'], href='../../athletes/%s.html' % athlete['_id']))

            f = open("../out/queryG/%s/%s.html" % (year, suitable), "w")
            f.write(doc.render())
            f.close()
            
        

    #Code to generate HTML doc for each year
    for year in dist.keys():

        doc = dominate.document(title=year)

        with doc:
            with div(id='header').add(ol()):
                for suitable in dist[year].keys():
                    li(a(suitable, href='../%s/%s.html' % (year,suitable) ))

        f = open("../out/queryG/%s/%s.html" % (year,year), "w")
        f.write(doc.render())
        f.close()

    
    #main HTML doc of the query
    doc = dominate.document(title='Distribuição por estatuto de federado em cada ano')

    with doc:
        with div(id='header').add(ol()):
            for year in dist.keys():
                li(a(year, href='../queryG/%s/%s.html' % (year,year)))

    f = open("../out/queryG/queryG.html", "w")
    f.write(doc.render())
    f.close()


def HTMLsGenerator(athletes):
    athletesGenerator(athletes)
    htmlMAIN()

    #a
    distA = distByDates(athletes)
    distByDatesHTML(distA)
    #b
    distB = distByYearAndGender(athletes)
    distByYearAndGenderHTML(distB)
    #c
    distC = distByYearAndSport(athletes)
    distByYearAndSportHTML(distC)
    #d
    distD = distByAgeAndGender(athletes)
    distByAgeAndGenderHTML(distD)
    #e
    distE = distByAddress(athletes)
    distByAddressHTML(distE)
    #f
    distF = distByYearAndFederated(athletes)
    distByYearAndFederatedHTML(distF)
    #g
    distG = distByYearAndSuitable(athletes)
    distByYearAndSuitableHTML(distG)
