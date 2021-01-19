"""
This script will print (std out) the sequence of a record with specified ID.

Input:
#######
    * -i : .fasta file to search for record

    * -v : ID to search for

Output:
#######

    * Sequence of record with specified ID

Usage:
#######
    * python fasta-parser.py --version *

    * This is the option that show you the program's version. *

    * python fasta-parser.py -h

    * This can show you some help information.

    * python fasta-parser.py -i <filename.fasta> -v <ID>

    *Runs program with specified file and ID*

"""

import sys
from argparse import ArgumentParser
from Bio import SeqIO  # pylint: disable=import-error

__version__ = "1.0"
__status__ = "Dev"


def main():
    """Find values with valid ID"""
    usage = "\n%prog  [options]"
    parser = ArgumentParser(description=usage)
    parser.add_argument('--version', '-V', action='version',
                        version="%(prog)s " + __version__)
    parser.add_argument("-i", "--fastaFile", action="store", dest="fastaFile",
                        help="Input FASTA file")
    parser.add_argument("-v", "--id", action="store", dest="Seq_ID", help="ID to check")

    options = parser.parse_args()
    for file in [options.fastaFile]:
        if not file:
            parser.print_help()
            sys.exit(0)

    fasta_file = options.fastaFile

    try:
        id_to_check = options.id
    except ValueError:
        parser.print_help()
        sys.exit(0)

    for record in SeqIO.parse(fasta_file, "fasta"):
        if record.id == id_to_check:
            print("%s" % record.seq)


if __name__ == '__main__':
    main()
