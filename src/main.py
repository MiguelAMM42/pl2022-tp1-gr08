import sys
from reader import reader
from queries import *

def main(csvFile):
    content = reader(csvFile)
    print(content)
    

if __name__== "__main__":
    main(sys.argv[1])