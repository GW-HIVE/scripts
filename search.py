#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################################################################
                            ##Accession Search##
""""Reads through the result files and populates dictionary with sample[accessionList] that are above detection threshhold """
################################################################################
#Declarations
import os, re, csv
my_dir = os.getcwd()
term = "cen"
gutDB = '/Users/hadley/BoxSync/Mazumdar_Lab/Otsuka/2019-Gut/analysis/blackGF.txt'
#thresh = 5
fileList = []
sampleDict = {}
#______________________________________________________________________________#
def createFileList(my_dir, term):
    """OS Walk to create file list based on a search term and a path"""
    
    for subdir, dirs, files in os.walk(my_dir):
        for file in files:
            if re.search(re.escape(term), file):
                result = os.path.join(subdir, file)
                fileList.append(result)
    return fileList
#______________________________________________________________________________#
def readCensusresultFile (file, dictionary, blacklist, threshold=10 ):
    """Takes an absolute file path, dictionary, a csv, and an optional threshold as input and returns a dictionary with taxId keys and accession number list as values"""
    sample = file.split('_')[-1].split('.')[0]
    with open (file, 'rU') as read:
        reader = csv.reader(read)
        for cell in reader:
            if cell[0] == '+': continue
            if cell[0] == '0': continue
            if cell[0] == 'id': continue
            accession = cell[1].split('.')[0]
            if accession in blacklist: continue
            if int(cell[2]) < threshold: continue
#                print "got one"
            if dictionary.has_key(accession):
                dictionary[accession].append(sample)
            else: dictionary[accession] = [sample]
    return dictionary
#______________________________________________________________________________#
def getGutDB ( file ):
    """reads the Gut DB accessions into a list for comparison"""
    gutDBList = []
    with open(file) as read:
        gutDBList = read.readlines()
    gutDBList = [word.strip() for word in gutDBList]
    return gutDBList
#______________________________________________________________________________#
def compare ( dictionary, list ):
    """checks the content of a dictionary against a list. Unique items are added to a new list"""
    newList = []
    for key in dictionary.keys():
        # print len(sampleDict[key])
        for accession in dictionary[key]:
            #print accession,
            if accession not in list: 
                # print accession, key
                if accession not in newList: newList.append(accession)
    return newList
#______________________________________________________________________________#
def main ():
    fileList = createFileList(my_dir, term)
    gutDBList = getGutDB(gutDB)
    for i in fileList:
        sample_dic = readCensusresultFile(i, sampleDict, gutDBList)
    for key in sample_dic:
#        if len(sample_dic[key]) > 1: 
        line = key+','
        for i in sample_dic[key]:
            line = line+i+','
        print line
    # # for i in sampleDict.keys(): print len(sampleDict[i])
    # print len(gutDBList), 'gut orgs'
    # newOrgs = compare(sampleDict, gutDBList)
    # print len(newOrgs)
    # with open('newAcc.txt', 'a') as file:
    #     for i in newOrgs:
    #         print i,
    #         file.write(i+'\n')
#______________________________________________________________________________#
if __name__ == '__main__': main()
