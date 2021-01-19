"""
This script will print(std out) all the fieldnames and field in the file path.

Input:
#######
-p : file path to check

Output:
#######
All the filenames and fields under CSV files in a specified path

Usage
#######
    1. python fastq-parser.py --version
    This is the option that show you the program's version.

    2. python fastq-parser.py -h
    This can show you some help information.

    3. python fastq-parser.py -i <filename.fastq>
    Runs program with specified file path
"""
import os
import csv
import glob
from argparse import ArgumentParser

__version__ = "1.0"
__status__ = "Dev"


def print_fieldnames(fieldnames_to_print):
    """Print all fieldnames given a list of fieldnames to print"""
    for field in fieldnames_to_print:
        file_names = fieldnames_to_print[field]
        if len(file_names) >= 1:
            for index, value in enumerate(file_names):
                for j in range(index, len(file_names)):
                    output = "%s.%s,%s.%s" % (value, field, file_names[j], field)
                    print(output)


def get_fieldnames(pattern_to_check):
    """Get all fieldnames of CSV files in a given path"""
    file_path_list = glob.glob(pattern_to_check)

    seen = {}
    for file_path in file_path_list:
        file_names = os.path.basename(file_path)
        with open(file_path, 'r') as file_reader:
            data_frame = csv.reader(file_reader, delimiter=',', quotechar='"')
            row_count = 0
            for row in data_frame:
                row_count += 1
                if row_count == 1:
                    for field in row:
                        if field not in seen:
                            seen[field] = []
                        seen[field].append(file_names)
    return seen


def main():
    """Find and print fieldnames"""

    usage = "\n%prog  [options]"
    parser = ArgumentParser(description=usage)
    parser.add_argument('--version', '-V', action='version',
                        version="%(prog)s " + __version__)
    parser.add_argument("-p", "--path", action="store", dest="path",
                        help="Path to check for CSV files")

    options = parser.parse_args()
    if options.path is not None:
        pattern = options.path + "/*.csv"
    else:
        pattern = "*.csv"

    print_fieldnames(get_fieldnames(pattern))


if __name__ == '__main__':
    main()
