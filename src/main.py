import sys
from reader import reader
from queries import *
from athletesGenerator import *
from htmlGenerator import *

def main(csvFile):
    content = reader(csvFile)
    #print(content)
    #athletesGenerator(content)
    dist = distByAddress(content)
    print(dist)
    doc = distByAddressHTML(dist)
    f = open("../out/index.html", "w")
    f.write(doc.render())
    f.close()
    

if __name__== "__main__":
    main(sys.argv[1])