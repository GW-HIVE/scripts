import os, sys
import string
import json
from optparse import OptionParser
import csv

__version__ = "1.0"
__status__ = "Dev"

"""
This script will transfer the .csv file to dataframe and print(std out) all the rows in the file with row number.
This script has three options, you can execute the script in three ways:
1. python csv-parser.1.py --version
This is the option that show you the program's version.
2. python csv-parser.1.py -h
This can show you some help information.
3. python csv-parser.1.py -i <filename.csv>
-i specifies input
Usage:
python csv-parser.1.py -i <filename.csv>
"""


def main():
    usage = "\n%prog  [options]"
    parser = OptionParser(usage, version="%prog " + __version__)
    parser.add_option("-i", "--infile", action="store", dest="infile", help="Input file")

    (options, args) = parser.parse_args()
    for file in ([options.infile]):
        if not (file):
            parser.print_help()
            sys.exit(0)

    inFile = options.infile

    with open(inFile, 'r') as FR:
        dataFrame = csv.reader(FR, delimiter=',', quotechar='"')
        rowCount = 0
        for row in dataFrame:
            rowCount += 1
            print(rowCount, row)


if __name__ == '__main__':
    main()
