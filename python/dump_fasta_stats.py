"""
This script will check the .fasta file that if there are duplicate IDs in the sequence.

Input:
#######
    * -i : .fasta file to check

Output:
#######

    * If duplicate IDs, output will be "Id repeated: bad fasta file".

    * If no duplicated IDs, output will be the number of sequence.

Usage:
#######
    1. python dump-fasta-stats.py --version

    This is the option that show you the program's version.

    2. python dump-fasta-stats.py -h

    This can show you some help information.

    3. python dump-fasta-stats.py -i <filename.fasta>
    This will check the .fasta file that if there are duplicate IDs in the sequence.

"""

import sys
from argparse import ArgumentParser
from Bio import SeqIO  # pylint: disable=import-error

__version__ = "1.0"
__status__ = "Dev"


def main():
    """
    Prints number of sequences.
    """
    usage = "\n%prog  [options]"
    parser = ArgumentParser(description=usage)
    parser.add_argument('--version', '-V', action='version',
                        version="%(prog)s " + __version__)
    parser.add_argument("-i", "--infile", action="store", dest="infile", help="FASTA input file")

    options = parser.parse_args()
    for file in [options.infile]:
        if not file:
            parser.print_help()
            sys.exit(0)

    in_file = options.infile

    print("Number of sequence:", count_sequences(in_file))


if __name__ == '__main__':
    main()


def count_sequences(file_to_check):
    """
    Count number of sequences.
    Inform the user if a ID repeats.
    """
    seen = {}
    count = 0
    for record in SeqIO.parse(file_to_check, "fasta"):
        if record.id in seen:
            print("Id repeated: bad fasta file")
            sys.exit()
        count += 1
        seen[record.id] = True
    return count
