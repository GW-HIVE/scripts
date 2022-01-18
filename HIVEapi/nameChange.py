#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

################################################################################
                            ##nameChange##
""""Takes a csv of [objectIds,Names] and submits a 'propset' request to update names"""
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
def nameChange ( file ):
    """submits propset change for i in list"""
    ids = {}
    with open(file, 'rU') as lst:
        read = csv.reader(lst)
        for i in read: 
            sample, objid = i[1], i[0]
            print sample, objid
            valuzPropSet =[
                ('cmdr','propset'),
                ('prop.'+str(objid)+'.name.1', sample)
            ]
            comand     = urllib.urlencode(valuzPropSet)
            response4  = opener.open(hive_URL, comand)
#______________________________________________________________________________#
def main ():
    response = logInHIVE (login,pwd)
    nameChange(lstfile)
#______________________________________________________________________________#
if __name__ == '__main__': main()