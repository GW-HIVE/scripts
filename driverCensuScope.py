#!/usr/bin/env python 
# -*- coding: utf-8 -*-
​
################################################################################
                        ## ##
""""Submit an instance of HIVE CenSuscope"""
################################################################################
​
from cookielib import CookieJar
import urllib
import urllib2
import re
import csv
import requests
import time
import os
import json
import sys
import argparse
​
hive_URL = 'https://hive.biochemistry.gwu.edu/dna.cgi?'
​
#______________________________________________________________________________#
def create_arg_parser():
    """creates arg parser for input file
    """
​
    parser = argparse.ArgumentParser(version='version 1.0', description='Submit an instance of HIVE CenSuscope. ')
    parser.add_argument('-i','--input', type=argparse.FileType('r'), help="input file. This should be a TSV with 3 columns == the sample name, file name, and HIVE obj_id")
    parser.add_argument('-db','--subjectDB', type=str, help="output file", default='513957')
    parser.add_argument('-p', '--paired end', help="output file", choices= ['y','n'], default='y')
    args = parser.parse_args
​
    return parser
#______________________________________________________________________________#
def logIn(  ):
    """Login to HIVE, start session. Returns cookies for session
    """
​
    login      = 'hadley_king@gwmail.gwu.edu'#raw_input('Enter Log In:\n')
    os.system("stty -echo")
    pwd        = 'Charles4'#raw_input('Enter Password:')
    os.system("stty echo")
    cj         = CookieJar()
    opener     = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    log_in     = str('api=0&cmdr=login&login='+login+'&pswd='+pwd)
    response   = opener.open(hive_URL, log_in)
    print "You are logged in to the HIVE..."
    return opener;
​
#______________________________________________________________________________#
def sampleLoad ( file ):
    """
    """
​
    samples = {}
    reader = csv.reader(file, delimiter="\t")
    for row in reader:
        if row[0] in samples:
            samples[row[0]].append((row[1]))
            samples[row[0]].append((row[2]))
            samples[row[0]].append((row[3])) #, row[2]])
        else:
            samples[row[0]] = [row[1], row[2]]
​
    # for k,v in samples.iteritems():
    #     print k, v[1], v[0], v[3], v[2]
​
    return samples
​
#______________________________________________________________________________#
def census( sample, designation, query1, query2, nt_db, opener ):
    """Submits the censuscope computation. Input is sample name, paired-end reads, and a db to align against. Returns the computation ID and the name"""
​
    print "Submitting CensuScope Process\n"
    censuName = sample+'_'+designation
    valuzCensus = [
        ('cmdr','-qpProcSubmit'),
        ('svc','svc-dna-screening'),
        ('prop.svc-dna-screening.action','2'),
        ('prop.svc-dna-screening._type','svc-dna-screening'),
        ('prop.svc-dna-screening.alignSelector.21','svc-align-blast'),
        ('prop.svc-dna-screening.automanual.22','0'),
        ('prop.svc-dna-screening.batch_svc.5','single'),
        ('prop.svc-dna-screening.blastWordSize.29','28'),
        ('prop.svc-dna-screening.CensusIterations.6','1'),
        ('prop.svc-dna-screening.CensuslimitIterations.7','5'),
        ('prop.svc-dna-screening.chunk_size.9','4000'),
        ('prop.svc-dna-screening.cutOffvalue.11','0.0005'),
        ('prop.svc-dna-screening.filterNs.12','1'),
        ('prop.svc-dna-screening.isPostponed.20.3','0'),
        ('prop.svc-dna-screening.name.1',censuName),
        ('prop.svc-dna-screening.query.1.1',query1),
        ('prop.svc-dna-screening.query.1.23',query2),
        ('prop.svc-dna-screening.reqPriority.20.7','0'),
        ('prop.svc-dna-screening.resultInQueryDir.26','0'),
        ('prop.svc-dna-screening.Sample.15','2500'),
        ('prop.svc-dna-screening.scissors.16','hiveseq'),
        ('prop.svc-dna-screening.selfStopping.27','0'),
        ('prop.svc-dna-screening.slice.17','0'),
        ('prop.svc-dna-screening.split.18','-'),
        ('prop.svc-dna-screening.storeAlignments.28','1'),
        ('prop.svc-dna-screening.subject',nt_db),
        ('prop.svc-dna-screening.submitter.33','dna-screening'),
        ('prop.svc-dna-screening.svc','dna-screening'),
        ('prop.svc-dna-screening.svcTitle','CensuScope'),
        ('prop.svc-dna-screening.systemVersion.20.11','1.1'),
        ('prop.svc-dna-screening.taxDepth.25','leaf'),
        ('prop.svc-dna-screening.textBasedColumn.31.1','0'),
        ('prop.svc-dna-screening.textBasedFileSeparator.31.2','1')
    ]
    
    comandCensus = urllib.urlencode(valuzCensus)
    print comandCensus
    response2 = opener.open(hive_URL, comandCensus)
    census_id = response2.read()
    census_id = census_id.split(',')[1]
    print "Your CensuScope ID is: ",census_id
    return census_id;
#______________________________________________________________________________#
def checkComputation( compID, opener ):
    """Checks for cmpletion of computation. Takes the Obj ID as input and holds script untill computation is complete"""
​
    valuzCheck = [
        ('cmdr','-qpRawCheck'),
        ('showreqs','0'),
        ('reqObjID',compID)
    ]
​
    comandCheck = urllib.urlencode(valuzCheck)
    stat = 0
    while stat <= 5:
        print "Progress report on object", compID
        response3 = opener.open(hive_URL, comandCheck)
        check = response3.read()
        stat = int(check.split('\n')[1].split(',')[6])
        prog = int(check.split('\n')[1].split(',')[8])
        if stat == 5: print "DONE!"; stat = 6; continue
        elif stat == 4: print "Process in Line"
        elif stat == 3: print "Process Running.", prog, "percent complete"
        elif stat == 2: print "Dont care"
        elif stat == 1: print "Process in submision"
        else: print "PROGRAM ERROR!!!! Unidentified Status Code"; break 
        time.sleep(30)
    return;
#______________________________________________________________________________#
def censusHitList( compID, censuName, opener ):
    """Downloads the hitlist result file and creates the HIVE Seq list. Input is object ID, Name, and blacklist. Returns list of indices for the HiveSeq Obj"""
​
    print "Getting Hit List from CensuScope...\n"
​
    valuzCensusList =[
        ('cmdr','alCount'),
        ('objs',compID)
    ]
​
    comand     = urllib.urlencode(valuzCensusList)
    response4  = opener.open(hive_URL, comand)
    censusHit  = response4.read()
    hitListCen = 'cen'+compID+'_'+censuName+'.csv'
    with open(hitListCen, 'w') as cenHitLst:
        cenHitLst.write(censusHit)
    print hitListCen, ' written to file'
​
    return 0
​
#______________________________________________________________________________#
def main():
    """
"""
    opener = logIn()
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    samples = sampleLoad(parsed_args.input)
#    logger = './temp/'+str(parsed_args.input.name)+'.txt'
#    sys.stdout = open(logger, "a")
​
#    print samples
    for k,v in samples.iteritems():
        print k, v[0], v[1], opener
    #     compID = census(k, v[4], v[1], v[3], parsed_args.subjectDB, opener)
    #     try: checkComputation(compID, opener)
    #     except: continue
        censusHitList(v[1], k, opener)
    print 'DONE!'
​
#______________________________________________________________________________#
if __name__ == "__main__":
    main()
