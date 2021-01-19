"""
Script will reprocess the vcf output of a HIVE Heptagon file to be in the appropriate vcf file
format per the standard.

Input:
""""""


Output:
"""""""


Usage:
""""""""


"""

import re


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
    with open('SNPSampleTabs.vcf') as in_file, open('SNPSampleReformatted.vcf', 'w') as out_file:
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
