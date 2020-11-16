### Script will reprocess the vcf output of a HIVE Heptagon file to be in the appropriate vcf file format per the standard.

import csv
import re

### Function to grab the chromosome number from the line, given HIVE's output style:
def chromGrabber(inLine):
	try:
		if 'chromosome x' in inLine or 'chromosome X' in inLine:
			chrom = 'X'
		elif 'chromosome y' in inLine or 'chromosome Y' in inLine:
			chrom = 'Y'
		elif 'mitochondrion' in inLine:
			chrom = 'MT'
		else:
			for i in range(1,23):
				pattern = ('chromosome '+str(i))
#				print ('Looking for', pattern, 'in', inLine)
				if re.search (pattern,inLine):
					chrom = i
					break
				else:
					pass
	except:
			print ('Found a non-conformer:', '\n', line)
	return chrom

### Read through file, ignore the headers, grab all of the relevant information, print it out in VCF format:
with open ('SNPSampleTabs.vcf') as inFile, open ('SNPSampleReformatted.vcf', 'w') as outFile:
#with open ('o29237-SNPprofile-all.vcf') as inFile, open ('SNPReformatted.vcf', 'w') as outFile:
		for line in inFile:
				if line[0] == '#':
					print (line, file=outFile, end='')
				else:
					try:
						position = re.split(r'\t', line)[1]
						seqid = re.split(r'\t', line)[0]
						ref = (re.split(r'\t', line)[3])
						alt = (re.split(r'\t', line)[4])
						qual = (re.split(r'\t', line)[5])
						seqfilter = (re.split(r'\t', line)[6])
						info = (re.split(r'\t', line)[7])
						chrom = chromGrabber(line)
						print (str(chrom)+'\t'+str(position)+'\t'+seqid+'\t'+ref+'\t'+alt+'\t'+str(qual)+'\t'+seqfilter+'\t'+info+'\n', file=outFile, end='')
					except:
						print ("Can't index, skipping...")

