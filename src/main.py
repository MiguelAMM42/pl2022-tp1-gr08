import sys
from reader import reader
from queries import *
from htmlGenerator import *

def main(csvFile):
    athletes = reader(csvFile)
    HTMLsGenerator(athletes)
    
    dist,stats = distByAgeAndGender(athletes)
    #print(distStats)
    print(stats)
    
    

if __name__== "__main__":
    main(sys.argv[1])