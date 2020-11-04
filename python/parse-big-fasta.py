#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
                        ##parse-big-fasta.py##
"""designed to parse the RVDB formatted FASTA headers so they can be interperated by HIVE-hexagon's tablequery"""
################################################################################

__version__="1.0"
__status__ = "Dev"

import re
import sys
import argparse

#______________________________________________________________________________#
def create_arg_parser():
    """"
    Creates and returns the ArgumentParser object.
    """

    parser = argparse.ArgumentParser(description='Fixes RVDB fasta file header format for HIVE-hexagon and tablequery.')

    parser.add_argument('inputFASTA',
                    help='Path to the input FASTA.')

    parser.add_argument('-o', '--output',
                    help='The output file for the new FASTA. If no output is provided the default will just append NEW to the file name')

    return parser

#______________________________________________________________________________#
def format_header ( parsed_args ):
    """
    parse the RVDB formatted FASTA headers and re-writes in desired format
    """

    accessions = []
    with open (parsed_args.inputFASTA) as infile:
        reader = infile.readlines()
        try:
            with open (parsed_args.output, 'w') as outfile:
                for line in reader:
                    if re.search('^>',line):
                        newline = line.split('|')[2:]
                        newline = '>gb|'+'|'.join(newline)
                        accessions.append(newline[0])
                        outfile.writelines(newline)
                    else: outfile.writelines(line)
        except:
            outfile = 'new_'+parsed_args.inputFASTA
            with open (outfile, 'w') as outfile:
                for line in reader:
                    if re.search('^>',line):
                        newline = line.split('|')[2:]
                        accessions.append(newline[0])
                        newline = '>gb|'+'|'.join(newline)
                        outfile.writelines(newline)
                    else: outfile.writelines(line)

    return accessions
#______________________________________________________________________________#

def main(  ):
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    accessions = format_header(parsed_args)
    print accessions
    with open ('accessions.txt', 'w') as acc:
        for a in accessions:
            acc.write(a+'\n')


#______________________________________________________________________________#
if __name__ == "__main__":
    main()
