# bibfix.py 
#  BibTeX bibliography fixer in Python
#  Usage: bibfix.py ifile.bib ofile.bib
#  TODO: user specified targets using a switch
#  TODO: option to manipulate file in place

import sys
import fileinput

def main(argv):
  if len(sys.argv) == 3:
    ifile = open(sys.argv[1], 'r')
    ofile = open(sys.argv[2], 'w')
    print 'Input file is: ', ifile.name
    print 'Output file is: ', ofile.name

    targets = ['Title = ', 'Author = ', 'Journal = ', 'Booktitle = ']
    
    for n, line in enumerate(ifile):
      for t in targets:
        if t in line:
          i = line.index(t)+len(t)
          newline = ''
          temp = list(line)
          while i < len(temp):  
            if temp[i].isupper():
              print 'Line: ', n, ' Found ', temp[i], 'at char ', i
              repstring = '{' + temp[i] + '}'
              temp[i] = repstring
              i += 2
            i += 1
          for x in temp:
            newline = newline + x
          line = newline;
          print "New Line: ", line
      ofile.write(line)        
    
    ifile.close
    ofile.close
  else:
    print 'Usage: bibfix.py ifile.bib ofile.bib'

if __name__ == "__main__":
  main(sys.argv[1:])



