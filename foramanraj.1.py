import os,sys
import string
import json
from optparse import OptionParser
import csv
import glob


__version__="1.0"
__status__ = "Dev"
"""
This script will print(std out) all the fieldnames and field in the file path.
input: 
all the <filename.csv> under folder you set.
Usage:
python foramanraj.py
"""

###############################
def main():



	pattern = "*.csv"
	filePathList = glob.glob(pattern)

	seen  = {}
	for filePath in filePathList:
		fNames = os.path.basename(filePath)
		with open(filePath, 'r') as FR:
        		dataFrame = csv.reader(FR, delimiter=',', quotechar='"')
        		rowCount = 0
			for row in dataFrame:
				rowCount += 1
				if rowCount == 1:
					for field in row:
						if field not in seen:
							seen[field] = []
						seen[field].append(fNames)

	for field in seen:
		fNamess = seen[field]
		if len(fNamess) > 1:
			for i in range(0, len(fNamess)):
				for j in range(i, len(fNamess)):
					o = "%s.%s,%s.%s" % (fNamess[i],field,fNames[j],field)
					print (o)


if __name__ == '__main__':
        main()


