"""
This script will print (std out) the fieldnames and the number of elements in each fieldname after
spited by deliminator


Input:
########
    * -i : CSV file to search

    * -d : Deliminator to split file by

Output:
########
    * Fieldnames and number of elements in each fieldname

Usage:
########

    * python dump-csv-stats.py --version

   *This is the option that show you the program's version.*

    * python dump-csv-stats.py -h

   *This can show you some help information.*

    * python dump-csv-stats.py -i <filename.csv> -d deliminator

   *Runs the program with the specified CSV file and deliminator.*
"""

import sys
from argparse import ArgumentParser
import csv

__version__ = "1.0"
__status__ = "Dev"


def main():
    """Find and print the number of elements in each fieldname"""
    usage = "\n%prog  [options]"
    parser = ArgumentParser(description=usage)
    parser.add_argument("-i", "--infile", action="store", dest="infile", help="CSV input file")
    parser.add_argument("-d", "--delim", action="store", dest="delim", help="Multi value column "
                                                                            "separator")
    parser.add_argument('--version', '-V', action='version',
                        version="%(prog)s " + __version__)

    options = parser.parse_args()
    for file in ([options.infile, options.delim]):
        if not file:
            parser.print_help()
            sys.exit(0)

    in_file = options.infile
    delim = options.delim

    seen = {}
    count = {}
    field_list = []
    with open(in_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        row_count = 0
        for row in csvreader:
            row_count += 1
            if row_count == 1:
                field_list = row
                for field_name in field_list:
                    count[field_name] = 0
                    seen[field_name] = {}
            else:
                for index, value in enumerate(row):
                    field_name = field_list[index]
                    value_list = value.strip().split(delim)

                    for val in value_list:
                        if val not in seen[field_name]:
                            count[field_name] += 1
                        seen[field_name][val] = True

    for field_name in field_list:
        print(field_name, count[field_name])


if __name__ == '__main__':
    main()
