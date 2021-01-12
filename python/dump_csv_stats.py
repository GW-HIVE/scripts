import sys
from argparse import ArgumentParser
import csv

__version__ = "1.0"
__status__ = "Dev"

"""
This script will print (std out) the fieldnames and the number of elements in each fieldname after spited by value.
This script has three options, you can execute the script in three ways:
1. python dump-csv-stats.py --version
This is the option that show you the program's version.
2. python dump-csv-stats.py -h
This can show you some help information.
3. python dump-csv-stats.py -i <filename.csv> -d value
-i specifies input
Usage:
python dump-csv-stats.py -i <filename.csv> -d value
"""


###############################
def main():
    """sample"""
    usage = "\n%prog  [options]"
    parser = ArgumentParser(description=usage)
    parser.add_argument("-i", "--infile", action="store", dest="infile", help="CSV input file")
    parser.add_argument("-d", "--delim", action="store", dest="delim", help="Multi value column "
                                                                            "separator")

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
                for j in range(0, len(row)):
                    field_name = field_list[j]
                    value_list = row[j].strip().split(delim)

                    for val in value_list:
                        if val not in seen[field_name]:
                            count[field_name] += 1
                        seen[field_name][val] = True

    for field_name in field_list:
        print(field_name, count[field_name])


if __name__ == '__main__':
    main()
