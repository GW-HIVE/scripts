#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

################################################################################
                            ##list_censusHIVE##
""""Submit a CensuScopr Job and waits for completion before submitting the next one in a list"""
################################################################################

from cookielib import CookieJar
import urllib, urllib2, re, csv, requests, time, os, json


login      = raw_input('Enter Email:')
os.system("stty -echo")
pwd        = raw_input('Enter Password:')
os.system("stty echo")
lstfile = '/Users/hadleyking/Downloads/reads_ids.csv'
gutDB   = '513957'
hive_URL   = 'https://hive.biochemistry.gwu.edu/dna.cgi?'
opener     = urllib2.build_opener(urllib2.HTTPCookieProcessor(CookieJar()))

#______________________________________________________________________________#
def logInHIVE ( login, pwd ):
    """Login to HIVE """
    log_in     = str('api=0&cmdr=login&login='+login+'&pswd='+pwd)
    response   = opener.open(hive_URL, log_in)
    print "login successfull"
    return response
#______________________________________________________________________________#
def readIDlist ( file ):
    """reads list of Obj Ids"""
    samples = {}
    with open(file, 'rU') as lst:
        read = csv.reader(lst)
        for i in read: 
            sample = i[1].split('_')[0]
            objid = i[0]
            if sample in samples.keys(): samples[sample].append(objid)
            else: samples[sample] = [objid]
    return samples
#______________________________________________________________________________#
def submitCensus ( sample, query1, query2, nt_db ):
    """Submits the API request for a CensuScope computation"""
    print "Submitting CensuScope Process\n"
    censuName = sample
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
#    print comandCensus
    response2 = opener.open(hive_URL, comandCensus)
    census_id = response2.read()
    census_id = census_id.split(',')[1]
    print "Your CensuScope ID is: ",census_id
    return census_id
#______________________________________________________________________________#
def checkProcess ( objID ):
    """Takes an object Id and checks for process status. Will loop until process is complete."""

    valuzCheck_census = [
        ('cmdr','-qpRawCheck'),
        ('showreqs','0'),
        ('reqObjID', objID)
    ]
    comandCheck = urllib.urlencode(valuzCheck_census)
    stat = 0
    while stat <= 5:
        print "Progress report on object", objID
        response3 = opener.open(hive_URL, comandCheck)
        check = response3.read()
        stat = int(check.split('\n')[1].split(',')[6])
        prog = int(check.split('\n')[1].split(',')[8])
        if stat == 5: print "DONE!"; stat = 6; continue
        elif stat == 4: print "Process in Line"
        elif stat == 3: print "Process Running.", prog, "percent complete"
        elif stat == 2: print "Dont care"
        elif stat == 1: print "Process in submision"
        else: print "PROGRAM ERROR!!!!"; break 
        time.sleep(120)
#______________________________________________________________________________#
def getHitList ( objID, sample ):
    """Uses ObjID to retreive the Census Hit List"""
    print "Getting Hit List from CensuScope...\n"

    valuzCensusList =[
        ('cmdr','alCount'),
        ('objs',objID)
    ]

    comand     = urllib.urlencode(valuzCensusList)
    response4  = opener.open(hive_URL, comand)
    censusHit  = response4.read()
    hitListCen = 'cen'+sample+'.csv'
    with open(hitListCen, 'w') as cenHitLst:
        cenHitLst.write(censusHit)
    print hitListCen, ' written to file'
    lines      = censusHit.split('\n')
#______________________________________________________________________________#
def main ():
    response = logInHIVE (login,pwd)
    objDict = readIDlist(lstfile)
    for sample in objDict.keys():
        print sample, objDict[sample][1], objDict[sample][0]
        census_id = submitCensus(sample, objDict[sample][1], objDict[sample][0], gutDB)
        checkProcess (census_id)
        getHitList (census_id, sample)
#______________________________________________________________________________#
if __name__ == '__main__': main()