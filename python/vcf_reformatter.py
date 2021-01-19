"""
Script will reprocess the vcf output of a HIVE Heptagon file to be in the appropriate vcf file
format per the standard.

Input:
########
* -i : specified file to reformat
* -o : specified output file


Output:
########
* Reformed vcf file

Usage:
########
    1. python vcf_reformatter.py --version
    This is the option that show you the program's version.

    2. python vcf_reformatter.py -h
    This can show you some help information.

    3. python vcf_reformatter.py -i <input.vcf> -o <output.vcf>
    Runs the program with specified input file, output file


"""

import re
from argparse import ArgumentParser


def chrom_grabber(inline):
    """
    Function to grab the chromosome number from the line, given HIVE's output style
    """
    try:
        if 'chromosome x' in inline.lower():
            chrom = 'X'
        elif 'chromosome y' in inline.lower():
            chrom = 'Y'
        elif 'mitochondrion' in inline:
            chrom = 'MT'
        else:
            for i in range(1, 23):
                pattern = ('chromosome ' + str(i))
                # print ('Looking for', pattern, 'in', inLine)
                if re.search(pattern, inline):
                    chrom = i
                    break
        return chrom
    except UnboundLocalError:
        print('Found a non-conformer:', '\n', inline)


def main():
    """Read through file, ignore the headers, grab all of the relevant information, print it out in
    VCF format."""
    usage = "\n%prog  [options]"
    parser = ArgumentParser(description=usage)  # Parser
    parser.add_argument('--version', '-V', action='version',
                        version="%(prog)s " + __version__)
    parser.add_argument("-i", "--input_file", action="store", dest="vcfFile", help="Input vcf file")
    parser.add_argument("-o", "--output_file", action="store", dest="vcfFile", help="Output vcf "
                                                                                    "file")

    options = parser.parse_args()

    with open(options.input_file) as in_file, open(options.outpit_file, 'w') as out_file:
        # with open ('o29237-SNPprofile-all.vcf') as inFile, open ('SNPReformatted.vcf',
        # 'w') as outFile:
        for line in in_file:
            if line[0] == '#':
                print(line, file=out_file, end='')
            else:
                try:
                    position = re.split(r'\t', line)[1]
                    seqid = re.split(r'\t', line)[0]
                    ref = (re.split(r'\t', line)[3])
                    alt = (re.split(r'\t', line)[4])
                    qual = (re.split(r'\t', line)[5])
                    seqfilter = (re.split(r'\t', line)[6])
                    info = (re.split(r'\t', line)[7])
                    chromo = chrom_grabber(line)
                    print(str(chromo) + '\t' + str(
                        position) + '\t' + seqid + '\t' + ref + '\t' + alt +
                          '\t' + str(qual) + '\t' + seqfilter + '\t' + info + '\n', file=out_file,
                          end='')
                except IndexError:
                    print("Can't index, skipping...")
