import csv

"""
This script will print(std out) all the rows with row number in a .csv file.
Usage:
python toy.py
"""
with open("A.csv", 'rb') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in csvreader:
		for j in range(0,len(row)):
			print (j,row[j])

