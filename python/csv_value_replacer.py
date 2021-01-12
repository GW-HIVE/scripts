import sys
from argparse import ArgumentParser

__version__ = "1.0"

"""
This script takes a CSV file and sums all numeric values in columns for rows with a specified header, mapping them to a
single row with a new replacement header.

Input: The index of the headers. 
       A CSV file of the form  -> header_to_sum_1;header_to_sum_2,replacement_header.
       The CSV file to change.
       The desired name of the new CSV file.
       
       
Output: Creates a new CSV file with the specified name.
"""


def main():
    usage = "\n%prog  [options]"
    parser = ArgumentParser(description=usage)
    parser.add_argument("-i", "--csvfile", action="store", dest="csvfile", help="Name of CSV file to be summed")
    parser.add_argument("-n", "--header_index", action="store", dest="header_index", help="Header Index")
    parser.add_argument("-d", "--mapping_dict", action="store", dest="mapping_dict",
                        help="Name of file containing mapping_dict")

    (options, args) = parser.parse_args()

    # First argument: index of the header value
    try:
        header_index = int(options.header_index)
    except ValueError:
        parser.print_help()
        sys.exit(0)

    # Second argument: name of the mapping file
    try:
        mapping_dict = eval(open(options.mapping_dict).read())
    except FileNotFoundError:
        parser.print_help()
        sys.exit(0)

    # Third argument:
    try:
        csv_as_list = eval(open(options.csvfile).read())
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
        # Skip blank rows
        if len(row) > 0:
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
                        for i in range(0, len(row)):
                            value = row[i]
                            if isinstance(value, float):
                                lines_to_append[mapping_dict[row[header_index]]][i] = value
                            else:
                                lines_to_append[mapping_dict[row[header_index]]][i] = ""
                    lines_to_append[mapping_dict[row[header_index]]][1] = mapping_dict[row[header_index]]
                # else, there is already an instance of a replacement row
                else:
                    # For each item in the row
                    for i in range(0, len(row)):
                        value = row[i]
                        # check if value is a float
                        if isinstance(value, float):
                            # sum it to current value in that column
                            lines_to_append[mapping_dict[row[header_index]]][i] += float(value)
                        # If item is non float and belongs to replacement value
                        elif row[header_index] == mapping_dict[row[header_index]]:
                            # Set text in replacement line to be text from replacement value
                            lines_to_append[mapping_dict[row[header_index]]][i] = value

            # If data does not contain a value to be summed, just add the new row to the new CSV contents
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
