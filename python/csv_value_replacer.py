"""
This script takes a CSV file and sums all numeric values in columns for rows with a specified
header, mapping them to a single row with a new replacement header.


Input:
########
* -i : CSV file to sum as a list
* -v : The index of the headers.
* -d : Mapping dictionary
    * *key*: value to sum to,
    * *value*: values to sum

Output:
########
* Summed CSV file

Usage:
########
1. python csv_value_replacer.py --version

        This is the option that show you the program's version.

2. python csv_value_replacer.py-h

        This can show you some help information.

3. python csv_value_replacer.py -i <filename.txt> -v <header_index> -d <mapping_dict>

        Runs the program given the specified CSV file.

"""
import sys
from argparse import ArgumentParser
import ast
__version__ = "1.0"


def main():
    """Sum CSV file"""
    usage = "\n%prog  [options]"
    parser = ArgumentParser(description=usage)
    parser.add_argument("-i", "--csvfile", action="store", dest="csvfile",
                        help="Name of CSV file to be summed")
    parser.add_argument("-v", "--header_index", action="store", dest="header_index",
                        help="Header Index")
    parser.add_argument("-d", "--mapping_dict", action="store", dest="mapping_dict",
                        help="Name of file containing mapping_dict")
    parser.add_argument('--version', '-V', action='version',
                        version="%(prog)s " + __version__)

    options = parser.parse_args()

    # First argument: index of the header value
    try:
        header_index = int(options.header_index)
    except ValueError:
        parser.print_help()
        sys.exit(0)

    # Second argument: name of the mapping file
    try:
        mapping_dict = ast.literal_eval(open(options.mapping_dict).read())
    except FileNotFoundError:
        parser.print_help()
        sys.exit(0)

    # Third argument:
    try:
        csv_as_list = ast.literal_eval(open(options.csvfile).read())
    except FileNotFoundError:
        parser.print_help()
        sys.exit(0)

    # Summed lines to add to new CSV file
    # Key: Replacement value
    # Value: Line to sum
    lines_to_append = {}

    # List containing all contents for new CSV file
    new_csv_file = []

    for row in csv_as_list:
        # If row contains data to be summed
        if row[header_index] in mapping_dict:
            # If there currently is no line replacement row, initialize one
            if mapping_dict[row[header_index]] not in lines_to_append:
                # If the row contains the data to sum to
                if row[header_index].strip(" ") == mapping_dict[row[header_index]]:
                    lines_to_append[mapping_dict[row[header_index]]] = row
                else:
                    # Create blank line
                    lines_to_append[mapping_dict[row[header_index]]] = [""] * len(row)
                    for index, value in enumerate(row):
                        if isinstance(value, float):
                            lines_to_append[mapping_dict[row[header_index]]][index] = value
                        else:
                            lines_to_append[mapping_dict[row[header_index]]][index] = ""
                lines_to_append[mapping_dict[row[header_index]]][1] = \
                    mapping_dict[row[header_index]]
            # else, there is already an instance of a replacement row
            else:
                # For each item in the row
                for index, value in enumerate(row):
                    # check if value is a float
                    if isinstance(value, float):
                        # sum it to current value in that column
                        lines_to_append[mapping_dict[row[header_index]]][index] += float(value)
                    # If item is non float and belongs to replacement value
                    elif row[header_index] == mapping_dict[row[header_index]]:
                        # Set text in replacement line to be text from replacement value
                        lines_to_append[mapping_dict[row[header_index]]][index] = value

        # If data does not contain a value to be summed, just add the new row to the new CSV
        # contents
        else:
            new_csv_file.append(row)

    # Add new lines at the end of the CSV contents
    for value in lines_to_append:
        new_csv_file.append((lines_to_append[value]))

    # Print contents to csv_file
    for line in new_csv_file:
        print(",".join((str(v) for v in line)))

if __name__ == "__main__":
    main()
