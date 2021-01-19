"""
This script takes a file containing a CSV as a list and returns transforms it into a dict

Input
#######
    * -i : File containing python list

    * -k : key_index (column that key for dictionary is in)

    * -v : value_index (column that values is in)

    * -d : Deliminator (deliminator between values OPTIONAL)

Output:
#######
    * A dict with key = key_index and value = value_index

Usage:
#######
    *python list_to_dict.py --version

    *This is the option that show you the program's version.*

    *python list_to_dict.py -h

    *This can show you some help information.*

    *python list_to_dict.py -i <filename.txt> -k <key_index> -v <value_index> -d <deliminator>

    *Runs program with specified file, key index, value index, and optional deliminator*
"""

import sys
from argparse import ArgumentParser
import ast

__version__ = "1.0"


def main():
    """
    Write list to dict
    """
    usage = "\n%prog  [options]"
    parser = ArgumentParser(description=usage)
    parser.add_argument("-i", "--infile", action="store", dest="infile",
                        help="File containing list")
    parser.add_argument("-d", "--delimator", action="store", dest="delimator",
                        help="Deliminator for dictionary values")
    parser.add_argument("-k", "--key", action="store", dest="key",
                        help="Index for key for dictionary")
    parser.add_argument("-v", "--value", action="store", dest="value",
                        help="Index for value for dictionary")
    parser.add_argument('--version', '-V', action='version',
                        version="%(prog)s " + __version__)
    options = parser.parse_args()

    # Dict to transform list into
    list_as_dict = {}

    try:
        original_list = ast.literal_eval(open(options.infile).read())
    except FileNotFoundError:
        parser.print_help()
        sys.exit()

    deliminator = None
    if options.delimator is not None:
        contains_deliminator = True
        deliminator = options.delimator
    else:
        contains_deliminator = False

    try:
        key_index = int(options.key)
    except ValueError:
        parser.print_help()
        sys.exit()

    try:
        value_index = int(options.value)

    except ValueError:
        parser.print_help()
        sys.exit()

    for row in original_list:
        if contains_deliminator:
            values = row[value_index].split(deliminator)
            list_as_dict[row[key_index]] = []
            for value in values:
                list_as_dict[row[key_index]].append(value)
        else:
            list_as_dict[row[key_index]] = [row[value_index]]

    print(list_as_dict)


if __name__ == '__main__':
    main()
