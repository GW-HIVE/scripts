import os,sys
import string
import csv
from optparse import OptionParser
from sas7bdat import SAS7BDAT


__version__="1.0"
__status__ = "Dev"

"""
This script will transfer a .sas file to a .csv file.
This script has three options, you can execute the script in three ways:
1. python sas7bdatTocsv.1.py --version
This is the option that show you the program's version.
2. python sas7bdatTocsv.1.py -h
This can show you some help information.
3. python sas7bdatTocsv.1.py -i <input.sas7bdat> -o <output.csv>
-i specifies input
Usage:
python sas7bdatTocsv.1.py -i <input.sas7bdat> -o <output.csv>
"""
###############################
def main():

        usage = "\n%prog  [options]"
        parser = OptionParser(usage,version="%prog " + __version__)
        parser.add_option("-i","--sasFile",action="store",dest="sasFile",help="Input sas file")
	parser.add_option("-o","--csvFile",action="store",dest="csvFile",help="Output csv file")


        (options,args) = parser.parse_args()
        for file in ([options.sasFile, options.csvFile]):
                if not (file):
                        parser.print_help()
                        sys.exit(0)

        sasFile = options.sasFile
	outFile = options.csvFile
	FW = csv.writer(open('outFile', 'wb'))
	with SAS7BDAT(sasFile) as f:
    		for row in f:
			FW.writerow(row)



if __name__ == '__main__':
        main()








