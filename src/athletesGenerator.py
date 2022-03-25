import dominate
from dominate.tags import *
import unicodedata

def athletesGenerator(athletes):
    for a in athletes:
        doc = dominate.document(title='TP1_PL_EMD')
   
        ##with doc.head:
        ##    link(rel='stylesheet', href='style.css')
        ##    script(type='text/javascript', src='script.js')

        with doc:
            with div(id='header').add(ol()):
                p(a['nome_primeiro'] + ' ' + a['nome_ultimo'])
                p(a['modalidade'])

            ##with div():
            ##    attr(cls='body')
            ##    p('Lorem ipsum..')


        fileName = "../out/athletes/" + a['_id'] + ".html"

        f = open(fileName, "w")
        f.write(doc.render())
        f.close()

        

