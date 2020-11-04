import os,sys
import string
import csv
from optparse import OptionParser
from sas7bdat import SAS7BDAT


__version__="1.0"
__status__ = "Dev"
"""
This script will transfer the .sas7bdat file to .csv format 
and print(std out) each line of the file(replace all the "," with ":" in each row).
This script has three options, you can execute the script in three ways:
1. python sas7bdatTocsv.2.py --version
This is the option that show you the program's version.
2. python sas7bdatTocsv.2.py -h
This can show you some help information.
3. python sas7bdatTocsv.2.py -i <filename.sas7bdat>
-i specifies input
Usage:
python sas7bdatTocsv.2.py -i <filename.sas7bdat>
"""

###############################
def main():

        usage = "\n%prog  [options]"
        parser = OptionParser(usage,version="%prog " + __version__)
        parser.add_option("-i","--sasFile",action="store",dest="sasFile",help="Input sas file")


        (options,args) = parser.parse_args()
        for file in ([options.sasFile]):
                if not (file):
                        parser.print_help()
                        sys.exit(0)

        sasFile = options.sasFile
	with SAS7BDAT(sasFile) as f:
    		for row in f:
			line = str(row[0])
			for i in range(1,len(row)):
				row[i] = str(row[i])
				row[i] = row[i].replace(",", ";")
				line += ", %s" % (str(row[i]))
			print (line)


if __name__ == '__main__':
        main()








