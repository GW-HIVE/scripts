#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

################################################################################
                            ##getDT_HIVE##
""""gets a DataType in JSON"""
################################################################################

from cookielib import CookieJar
import urllib, urllib2, re, csv, requests
hive_URL  = 'https://hive.biochemistry.gwu.edu/dna.cgi?'
hiveType = raw_input('Name of type?\n')
f = str('def.'+hiveType+'.json')

writer = open(f, 'w')

email     = raw_input('Enter Email:')
pwd       = raw_input('Enter Password:')
cj        = CookieJar()
opener    = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
log_in    = 'api=0&cmdr=login&login='+email+'&pswd='+pswd
response  = opener.open(hive_URL, log_in)
(hive_URL, log_in)

print "You are logged in to the HIVE..."

valuz = [
    ('cmdr','propspec'),
    ('type',hiveType),
    ('mode','json')
]

comand = urllib.urlencode(valuz)
response2 = opener.open(hive_URL, comand)
writer.write(response2.read())