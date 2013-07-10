# bibfix.py 
#  BibTeX bibliography fixer in Python
#  Usage: bibfix.py ifile.bib ofile.bib

#  TODO: mode to change file in place

import sys, argparse
import fileinput


def main(argv, verbose, targets, lifile, lofile):
  ifile = open(lifile, 'r')
  ofile = open(lofile, 'w')
  print 'Input file is: ', ifile.name
  print 'Output file is: ', ofile.name
    
  for n, line in enumerate(ifile):
    for t in targets: 
      if t in line:
        i = line.index(t)+len(t)
        newline = ''
        temp = list(line)
        while i < len(temp):  
          if temp[i].isupper():
            if verbose:
              print 'Line: ', n, ' Found ', temp[i], 'at char ', i
            repstring = '{' + temp[i] + '}'
            temp[i] = repstring
            # i += 1
          i += 1
        for x in temp:
          newline = newline + x
        line = newline;
        if verbose:
          print "New Line: ", line
    ofile.write(line)        
                    
  ifile.close
  ofile.close
  print "Done..."
  return 0

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Preserve capitals in BibTeX file")
  parser.add_argument('-v', '--verbose', 
                      help='Verbose mode',
                      action='store_true')
  parser.add_argument('-t', '--target', 
                      nargs='*',
                      help='Add custom hooks to look for, Defaults are: Title, Author, Journal, Booktitle')
  parser.add_argument("ifile", help="input bib file")
  parser.add_argument("ofile", help="output bib file")
  args = parser.parse_args()

  if args.target:
    targets = args.target
    print 'Targets are: ', targets
  else:
    targets = ['Title = ', 'Author = ', 'Journal = ', 'Booktitle = ']
    print 'Targets defaulted to ', targets

  if args.verbose:
    print 'verbose is true'

  main(sys.argv[1:], args.verbose, targets, args.ifile, args.ofile)



