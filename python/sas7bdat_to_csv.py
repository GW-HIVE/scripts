"""
This script will transfer a .sas file to a .csv file.
This script has three options, you can execute the script in three ways:
1. python sas7bdat_to_csv.py --version
This is the option that show you the program's version.
2. python sas7bdat_to_csv.py -h
This can show you some help information.
3. python sas7bdat_to_csv.py -i <input.sas7bdat> -o <output.csv>
-i specifies input
Usage:
python sas7bdat_to_csv.py -i <input.sas7bdat> -o <output.csv>
"""
import csv
import sys
from argparse import ArgumentParser
from sas7bdat import SAS7BDAT   # pylint: disable=import-error

__version__ = "1.0"
__status__ = "Dev"


def main():
    """
    Transfer a .sas7bdat file to a .csv file.
    """

    usage = "\n%prog  [options]"
    parser = ArgumentParser(description=usage)  # Parser
    parser.add_argument("-i", "--sasFile", action="store", dest="sasFile", help="Input sas file")
    parser.add_argument("-o", "--csvFile", action="store", dest="csvFile", help="Output csv file")
    parser.add_argument("-d", "--delim", action="store", dest="delim", help="Optional deliminator "
                                                                            "for output file. "
                                                                            "If not provided, "
                                                                            "default is comma.")

    options = parser.parse_args()
    for file in ([options.sasFile, options.csvFile]):
        if not file:
            parser.print_help()
            sys.exit(0)

    sas_file = options.sasFile
    out_file = options.csvFile
    file_writer = csv.writer(open(out_file, 'wb'))
    with SAS7BDAT(sas_file) as file:
        for row in file:
            line = str(row[0])
            for i in range(1, len(row)):
                row[i] = str(row[i])
                if options.delim is not None:
                    row[i] = row[i].replace(",", options.delim)
                line += ", %s" % (str(row[i]))
            file_writer.writerow(line)


if __name__ == '__main__':
    main()
