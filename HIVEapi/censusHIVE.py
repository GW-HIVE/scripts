#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

################################################################################
                            ##censusHIVE##
""""Submit a CensuScopr Job"""
################################################################################

from cookielib import CookieJar
import urllib, urllib2, re, csv, requests, json, os
from urllib2 import URLError
from bs4 import BeautifulSoup

hive_URL   = 'https://hive.biochemistry.gwu.edu/dna.cgi?'
os.system("stty -echo")
email      = raw_input('Enter Email:')
pwd        = raw_input('Enter Password:')
os.system("stty echo")
cj         = CookieJar()
opener     = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
log_in     = str('api=0&cmdr=login&login='+email+'&pswd='+pwd)
response   = opener.open(hive_URL, log_in)

print "You are logged in to the HIVE..."

valuz = [
('prop.svc-align-blast.name.1','filteredHMB01-1-contig.fa versus hgdbv1.6'),
('prop.svc-align-blast.alignSelector.36','svc-align-blast'),
('prop.svc-align-blast.force_reindex.37','0'),
('prop.svc-align-blast.submitter.40','dna-hexagon&cmdMode','blast-bacteria'),
('prop.svc-align-blast.maxNumberQuery.15','all'),
('prop.svc-align-blast.batch_svc.6','single'),
('prop.svc-align-blast.blastProgram.7','blastn'),
('prop.svc-align-blast.evalueFilter.12','1e-4'),
('prop.svc-align-blast.cmdLine.9','-task megablast -num_threads 1'),
('prop.svc-align-blast.scissors.26','hiveseq'),
('prop.svc-align-blast.complexityRefEntropy.10.1.0','1.2'),
('prop.svc-align-blast.complexityRefWindow.10.1.0','30'),
('prop.svc-align-blast.acceptNNNQuaTrheshold.10.1.0','1'),
('prop.svc-align-blast.complexityEntropy.10.0.0','1.2'),
('prop.svc-align-blast.complexityWindow.10.0.0','30'),
('prop.svc-align-blast.maximumPercentLowQualityAllowed.10.0.0','0'),
('prop.svc-align-blast.keepAllMatches.13','4'),
('prop.svc-align-blast.maxHitsPerRead.14','200'),
('prop.svc-align-blast.minMatchLen.16.0','75'),
('prop.svc-align-blast.minMatchUnit.16.0','0'),
('prop.svc-align-blast.maxMissQueryPercent.17.0','15'),
('prop.svc-align-blast.considerGoodSubalignments.17.0','1'),
('prop.svc-align-blast.num_alignments.19','10'),
('prop.svc-align-blast.random_seed.23','0'),
('prop.svc-align-blast.resolveConflicts.24.1','2'),
('prop.svc-align-blast.resolveConflictsScore.24.2','2'),
('prop.svc-align-blast.resolveConfictsUnique.24.0','1'),
('prop.svc-align-blast.scoreFilter.27','None'),
('prop.svc-align-blast.splitType.31.3','sequences'),
('prop.svc-align-blast.nrepeat.31.0','1'),
('prop.svc-align-blast.splitField.31.1','query'),
('prop.svc-align-blast.splitSize.31.2','4000'),
('prop.svc-align-blast.isPostponed.34.3','0'),
('prop.svc-align-blast.reqPriority.34.7','0'),
('prop.svc-align-blast.split.30','query'),
('prop.svc-align-blast.seedSize.28','28'),
('prop.svc-align-blast.slice.29','4000'),
('prop.svc-align-blast.query.1.1','557823'),
('prop.svc-align-blast.subject.1.1','557831'),
('prop.svc-align-blast.svc','dna-alignx')
]

comand = urllib.urlencode(valuz)
print comand
response2 = opener.open(hive_URL, comand)
new_id = response2.read()
new_id = new_id.split(',')[1]
print new_id

