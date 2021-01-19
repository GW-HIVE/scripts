"""This script will add double quotes to all values in a csv file. If a value is already quoted,
quotes will not be added to that value. If there is quoted text within a value the quoted text
will now have two sets of quotes e.g. ""quoted text"".

Input:
#######

* -i : the path to the original csv file to edit.

* -o : the path to the output csv file that will contain the edits.

Output:
#######

* The edited csv file to the path specified in output_file argument.

Usage:
#######

    * python quote_csv.py --version

    *This is the option that show you the program's version.*

    * python quote_csv.py -h

    *This can show you some help information.*

    * python quote_csv.py -i <filename.csv> -o <output_file.csv>

    *Runs program with specified file to quote and output file*

"""

# For editing the csv file.
import csv

# For taking command line arguments.
import argparse

__version__ = "1.0"
__status__ = "Dev"


def main(csv_file, output_file):
    """Quote original CSV file and write contents to specified output file"""
    # Read the original csv file and load data into a list.
    with open(csv_file, 'r') as file:
        original_file = csv.reader(file)

        # Create a list to hold the data.
        data = []

        # Add to the data list.
        for row in original_file:
            data.append(row)

    # Write data list to the new file with quotes around all values.
    with open(output_file, 'w') as out_file:
        writer = csv.writer(out_file, quoting=csv.QUOTE_ALL)
        writer.writerows(data)

    # Output message.
    print('csv file ' + csv_file + ' written with quotes to ' + output_file)


# Command line arguments.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Commands for mapping script.')
    parser.add_argument('--csv_file', '-i',
                        help='The csv file')
    parser.add_argument('--output_file', '-o',
                        help='The output file')
    parser.add_argument('--version', '-V', action='version',
                        version="%(prog)s " + __version__)
    args = parser.parse_args()

    main(args.csv_file, args.output_file)
