import os,sys
import string
import json
from optparse import OptionParser
import csv

__version__="1.0"
__status__ = "Dev"

"""
This script will print (std out) the fieldnames and the number of elements in each fieldname after spited by value.
This script has three options, you can execute the script in three ways:
1. python dump-csv-stats.py --version
This is the option that show you the program's version.
2. python dump-csv-stats.py -h
This can show you some help information.
3. python dump-csv-stats.py -i <filename.csv> -d value
-i specifies input
Usage:
python dump-csv-stats.py -i <filename.csv> -d value
"""
###############################
def main():

	usage = "\n%prog  [options]"
	parser = OptionParser(usage,version="%prog " + __version__)
	parser.add_option("-i","--infile",action="store",dest="infile",help="CSV input file")
	parser.add_option("-d","--delim",action="store",dest="delim",help="Multi value column separator")


	(options,args) = parser.parse_args()
	for file in ([options.infile, options.delim]):
		if not (file):
			parser.print_help()
			sys.exit(0)


	inFile = options.infile
	delim = options.delim

	seen = {}

	count = {}
	fieldList = []
	with open(inFile, 'r') as csvfile:
        	csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        	rowCount = 0
		for row in csvreader:
			rowCount += 1
			if rowCount == 1:
				fieldList = row
				for fieldName in fieldList:
					count[fieldName] = 0
					seen[fieldName] = {}
			else:
				for j in range(0, len(row)):
					fieldName = fieldList[j]
					valueList = row[j].strip().split(delim)

					for val in valueList:
						if val not in seen[fieldName]:
							count[fieldName] += 1
						seen[fieldName][val] = True


	for fieldName in fieldList:
		print (fieldName, count[fieldName])



if __name__ == '__main__':
        main()


