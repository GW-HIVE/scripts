"""
This script will print (std out) the sequence of a record with id equals "ENST00000357654".
This script has three options, you can execute the script in three ways:
1. python fasta-parser.py --version
This is the option that show you the program's version.
2. python fasta-parser.py -h
This can show you some help information.
3. python fasta-parser.py -i <filename.fasta>
-i specifies input
Usage:
python fasta-parser.py -i <filename.fasta>
"""

import sys
from argparse import ArgumentParser
from Bio import SeqIO  # pylint: disable=import-error

__version__ = "1.0"
__status__ = "Dev"


def main():
    """sample"""
    usage = "\n%prog  [options]"
    parser = ArgumentParser(description=usage)
    parser.add_argument("-i", "--fastaFile", action="store", dest="fastaFile",
                        help="Input FASTA file")
    parser.add_argument("-d", "--id", action="store", dest="Seq_ID", help="ID to check")

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