#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

################################################################################
                            ##docHIVE##
""""gets a file based on HIVE id"""
################################################################################

from cookielib import CookieJar
import urllib, urllib2, re, csv, requests
from urllib2 import URLError
#from bs4 import BeautifulSoup

hive_URL  = 'https://hive.biochemistry.gwu.edu/dna.cgi?'
email = ''
pswd = ''
cj        = CookieJar()
opener    = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
log_in    = 'api=0&cmdr=login&login='+email+'&pswd='+pswd
response  = opener.open(hive_URL, log_in)


print "You are logged in to the HIVE..."

valuz = [
    ('cmdr','alCount'),
    ('objs','540758'),
    ('down','1')
]

comand = urllib.urlencode(valuz)
response2 = opener.open(hive_URL, comand)
print response2.read()

# cmdr=objFile
# ids=<csv ids>
# filename=<filename>
# propname=<propname>
#
# https://hive.biochemistry.gwu.edu/dna.cgi?
# cmd=alCount
# start=0
# cnt=0
# objs=540758
# down=1