import sys
from reader import reader
from queries import *
from htmlGenerator import *

def main(csvFile):
    content = reader(csvFile)
    #print(content)

    (dist,distStats) = distByAgeAndGender(content)
    print(distStats)


    #print(content)
    #athletesGenerator(content)
    #dist = distByAddress(content)
    #print(dist)
    #distByAddressHTML(dist)

    #dist2 = distByDates(content) 
    #distByDatesHTML(dist2)

    #dist3 = distByYearAndGender(content)
    #distByYearAndGender(dist3)

    #htmlMAIN()
    
    

if __name__== "__main__":
    main(sys.argv[1])