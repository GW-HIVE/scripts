#DRM formula script
'''
This script is meant to synthesize wildtype and mutation information per each row of the DRM table and format the information into the JavaScript line necessary for the HIVE annotation table.
'''

import pandas as pd 

# access the csv file 

# path = "C:/Users/Emily/OneDrive/Desktop/School/Thesis/DRM_mock_table.csv"

path = "C:/Users/Emily/OneDrive/Desktop/School/Thesis/DRM_table_final.csv"

drmFile = pd.read_csv(path, delimiter = ',')

# check to see if the file has been located by printing the column headers

print(drmFile.columns)

# extract cell values from rows and make into a single row 

drmFile['formula'] = "${seq}== '" + drmFile['refseq_protein_accession'].astype(str) + "' && (int)${pos}==" + drmFile['amino_acid_pos_refseq'].astype(str) + " && ${wt}=='" + drmFile['wt_amino_acid'] + "' && ${mut}=='" + drmFile['mut_amino_acid'] + "'"

print(drmFile['formula'])

# save as new csv file with formula column

drmFile.to_csv('drm_table_export.csv', index=False)

