with open ('DRM_Report.csv', 'w+') as outFile:
	with open ('sampleOutput.csv', 'r') as inFile:
		with open ('DRMLookupTable.csv', 'r') as lookup:
			lookupTable = list (lookup)
			for line in inFile:
				if line[0] == '#':
					print (line.strip(), file = outFile)
				else:
					number = line.split(',')[0]
					hit = line.split(',')[1]
					pos = line.split(',')[2]
					wt = line.split(',')[3]
					mut = line.split(',')[4]
					cds = line.split(',')[5]
					description = line.split(',')[6]
					for row in lookupTable:
						if row.split(',')[0] == 'HIV Gene region':
							pass
						else:
							wildtype = row.split(',')[1]
							position = row.split(',')[4]
							mutation = row.split(',')[6]
							newPos = row.split(',')[2]
							if pos == position and wt == wildtype and mut == mutation:
								print (number + ',' + hit + ',' + newPos + ',' + wt + ',' + mut + ',' + cds + ',' + description.strip(), file = outFile)

