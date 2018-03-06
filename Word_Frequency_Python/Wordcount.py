import getopt, sys, os
import re
from collections import Counter

def usage():
  print 'Usage: '+sys.argv[0]+' -f <file1>'
  sys.exit(1)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'hf:', ['help', 'file'])
        if not opts:
            print 'No parameters supplied'
            usage()
    except getopt.GetoptError, e:
        print e
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt == '-f':
            fIn = argv[1]
            print fIn


    try:
        with open(fIn, 'r') as f:
            file_content = f.read()
        print ("read file " + fIn)
        if not file_content:
            print ("no data in file " + fIn)
        ##file_content = "name,phone,address\n"
    except IOError as e:
        print ("I/O error({0}): {1}".format(e.errno, e.strerror))
        sys.exit(1)
    except: #handle other exceptions such as attribute errors
        print ("Unexpected error:", sys.exc_info()[0])
        sys.exit(1)

    #collect all the words from the file in lower case
    words = re.findall(r'\w+', open(fIn).read().lower())
    #counter from library is used to fetch most common words
    topten=Counter(words).most_common(10)
    print ( "Top ten most recurring words in the file :")
    print (topten)

if __name__ == "__main__":
    main(sys.argv[1:])
