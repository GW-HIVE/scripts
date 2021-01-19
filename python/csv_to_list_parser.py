"""
This script will transfer a .csv file to dataframe and print (std out) a list. Automatically tries
to convert numerical values into floats.


Input:
########
* **-i **: CSV to print

Output:
########
* CSV as list

Usage
########
1. python csv_to_list_parser.py --version

        This is the option that show you the program's version.

2. python csv_to_list_parser.py -h

        This can show you some help information.

3. python csv_to_list_parser.py -i <filename.csv>

        Runs the program given the specified CSV file.
"""

import sys
from argparse import ArgumentParser
import csv

__version__ = "1.0"
__status__ = "Dev"


def main():
    """
    Writes CSV to list
    """

    usage = "\n%prog  [options]"
    parser = ArgumentParser(description=usage)
    parser.add_argument("-i", "--infile", action="store", dest="infile", help="Input file")
    parser.add_argument('--version', '-V', action='version',
                        version="%(prog)s " + __version__)
    options = parser.parse_args()
    for file in [options.infile]:
        if not file:
            parser.print_help()
            sys.exit(0)

    in_file = options.infile

    csv_as_list = []
    with open(in_file) as file_reader:
        line_to_append = []
        data_frame = csv.reader(file_reader, delimiter=',', quotechar='"')
        for row in data_frame:
            for value in row:
                try:
                    line_to_append.append(float(value))
                except ValueError:
                    line_to_append.append(value)
            csv_as_list.append(line_to_append)
            line_to_append = []
    print(csv_as_list)


if __name__ == '__main__':
    main()
