"""
Input:

csv_file: the path to the original csv file to edit.

output_file: the path to the output csv file that will contain the edits. File does not need to
already exist.

Output:

The edited csv file to the path specified in output_file argument.
"""

# For editing the csv file.
import csv

# For taking command line arguments.
import argparse


def main(csv_file, output_file):
    """sample"""
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
    args = parser.parse_args()

    main(args.csv_file, args.output_file)
