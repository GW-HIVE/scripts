#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

################################################################################
                            ##apiHIVE##
""""returns CensuScope HitList file"""
################################################################################

from cookielib import CookieJar
import urllib, urllib2, re, csv, requests, os
from urllib2 import URLError
from bs4 import BeautifulSoup

hive_URL   = 'https://hive.biochemistry.gwu.edu/dna.cgi?'
os.system("stty -echo")
email      = = raw_input('Enter Email:')
pwd        = raw_input('Enter Password:')
os.system("stty echo")
cj         = CookieJar()
opener     = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
log_in     = str('api=0&cmdr=login&login='+email+'&pswd='+pwd)
response   = opener.open(hive_URL, log_in)

print "You are logged in to the HIVE..."

hiveseqQry = '515362,1,1;515593,1,1;516397,1,1;516398,1,1;516690,1,1;516692,1,1;523037,1,1;532707,1,1;536714,1,1;538148,1,1;538163,1,1;538175,1,1;538322,1,1;538326,1,1;538364,1,1;538507,1,1;538617,1,1;538619,1,1;538620,1,1;538623,1,1;538625,1,1;538626,1,1;538629,1,1;538630,1,1;538633,1,1;538634,1,1;538637,1,1;538638,1,1;538641,1,1;538642,1,1;538645,1,1;538646,1,1;538649,1,1;538650,1,1;538652,1,1;538654,1,1;538656,1,1;538658,1,1;538662,1,1;538665,1,1;538666,1,1;538668,1,1;538671,1,1;538673,1,1;538674,1,1;538689,1,1;538690,1,1;538691,1,1;538692,1,1;538697,1,1;538698,1,1;538699,1,1;538701,1,1;538705,1,1;538706,1,1;538707,1,1;538708,1,1;538714,1,1;538715,1,1;538717,1,1;538722,1,1;538723,1,1;538724,1,1;538725,1,1;538730,1,1;538731,1,1;538732,1,1;538734,1,1;538738,1,1;538739,1,1;538740,1,1;538741,1,1;538746,1,1;538747,1,1;538748,1,1;538749,1,1;538754,1,1;538755,1,1;538757,1,1;538758,1,1;538883,1,1;538885,1,1;538989,1,1;538995,1,1;539002,1,1;539006,1,1;539019,1,1;539323,1,1;539455,1,1;539457,1,1;539463,1,1;539464,1,1;539465,1,1;539470,1,1;539547,1,1;539548,1,1;539555,1,1;539556,1,1;539600,1,1;539602,1,1;539610,1,1;539618,1,1;539620,1,1;539624,1,1;539625,1,1;539629,1,1;539632,1,1;539657,1,1;539693,1,1;539696,1,1;539737,1,1;539738,1,1;539740,1,1;539745,1,1;539749,1,1;539752,1,1;539753,1,1;539754,1,1;539756,1,1;539760,1,1;539769,1,1;539837,1,1;539867,1,1;539894,1,1;539896,1,1;540017,1,1;540018,1,1;540019,1,1;540020,1,1;540025,1,1;540026,1,1;540028,1,1;540035,1,1;540041,1,1;540102,1,1;540173,1,1;540362,1,1;540368,1,1;540369,1,1;540530,1,1;540532,1,1;540584,1,1;540588,1,1;540652,1,1;540653,1,1;540791,1,1;540976,1,1;541019,1,1;546774,1,1;546776,1,1;546777,1,1;546778,1,1;546782,1,1;553136,1,1;553362,1,1;553364,1,1;553365,1,1;553368,1,1;553370,1,1;553371,1,1;553372,1,1;553375,1,1;553378,1,1;553380,1,1;553382,1,1;553383,1,1;553386,1,1;553387,1,1;553388,1,1;553389,1,1;553390,1,1;553391,1,1;'

valuz = [
('cmdr','-qpProcSubmit'),
('svc','dna-hiveseq'),
('raw','1'),
('prop.svc-hiveseq.name.1','testHiveseqName'),
('prop.svc-hiveseq.AlgorithmsName.11.0','0'),
('prop.svc-hiveseq.lowcomplexityactive.12.0','0'),
('prop.svc-hiveseq.lowcomplexityWindow.12.0','15'),
('prop.svc-hiveseq.lowcomplexityEntropy.12.0','1'),
('prop.svc-hiveseq.lowcomplexityOption.12.0','0'),
('prop.svc-hiveseq.AdaptersFilter.13','0'),
('prop.svc-hiveseq.adaptersactive.13.0','0'),
('prop.svc-hiveseq.adaptersObjId.13.0','0'),
('prop.svc-hiveseq.adaptersReverse.13.0.0','0'),
('prop.svc-hiveseq.adaptersComplement.13.0.1','0'),
('prop.svc-hiveseq.adaptersMaxmissmatches.13.0','2'),
('prop.svc-hiveseq.adaptersMinLength.13.0','10'),
('prop.svc-hiveseq.primersactive.17.0','0'),
('prop.svc-hiveseq.primersReverse.17.0.0','0'),
('prop.svc-hiveseq.primersComplement.17.0.1','0'),
('prop.svc-hiveseq.primersKeep.17.0','0'),
('prop.svc-hiveseq.primersMaxmissmatches.17.0','2'),
('prop.svc-hiveseq.primersMinLength.17.0','100'),
('prop.svc-hiveseq.QualityFilter.19','0'),
('prop.svc-hiveseq.qualityactive.19.0','0'),
('prop.svc-hiveseq.qualityPercentage.19.0','100'),
('prop.svc-hiveseq.qualityThreshold.19.0','50'),
('prop.svc-hiveseq.trimMinimum.20.0','-1'),
('prop.svc-hiveseq.trimMaximum.20.0','-1'),
('prop.svc-hiveseq.removeMin.21.0.0','-1'),
('prop.svc-hiveseq.removeMax.21.0.0','-1'),
('prop.svc-hiveseq.lengthSeqFilter.16','0'),
('prop.svc-hiveseq.minimumSeqLength.16.0','0'),
('prop.svc-hiveseq.idfilteractive.15.0','0'),
('prop.svc-hiveseq.idlistObjId.15.0','0'),
('prop.svc-hiveseq.listExclusion.15.0','0'),
('prop.svc-hiveseq.randomizerNumValue.22.0','100'),
('prop.svc-hiveseq.randomizerNoise.22.1','0'),
('prop.svc-hiveseq.randomizerMinLength.22.2','100'),
('prop.svc-hiveseq.randomizerMaxLength.22.3','100'),
('prop.svc-hiveseq.randomizerRevComp.22.6','0'),
('prop.svc-hiveseq.randLengthNorm.22.7','1'),
('prop.svc-hiveseq.seqExclusionOption.23.1','0'),
('prop.svc-hiveseq.seqExclusionRevComp.23.2','0'),
('prop.svc-hiveseq.hiveseqQry.24',hiveseqQry),
('prop.svc-hiveseq.inputMode.25','0'),
('prop.svc-hiveseq.pecPairEndFile.18.0','0'),
('prop.svc-hiveseq.pecMinMatchLen.18.0','15'),
('prop.svc-hiveseq.pecQualities.18.0','1'),
('prop.svc-hiveseq.pecKeepAlignments.18.0','0'),
('prop.svc-hiveseq.denovoExtSizemer.14.0','16'),
('prop.svc-hiveseq.denovoExtSizeFilter.14.0','0'),
('prop.svc-hiveseq.denovoExtRptFilter.14.0','0'),
('prop.svc-hiveseq.denovoExtFirstStage.14.0','1'),
('prop.svc-hiveseq.denovoOutFilterLength.14.0','1000'),
('prop.svc-hiveseq.denovoMissmatchesPercentage.14.0','2'),
('prop.svc-hiveseq.maxNumberQueryForHiveseq.25','-1'),
('prop.svc-hiveseq.inputMode.27.0','1'), #
('prop.svc-hiveseq.isFastQFile.26.0','1'),
('prop.svc-hiveseq.keepOriginalID.26.1','1'),
('prop.svc-hiveseq.appendLength.26.2','1'),
('prop.svc-hiveseq.isHiveseq.26.3','0'),
('prop.svc-hiveseq.isRevComp.26.4','0'),
('prop.svc-hiveseq.submitter.29','dna-hiveseq'),
('prop.svc-hiveseq._type','svc-hiveseq'),
('prop.svc-hiveseq.parent_proc_ids.9','3101923'),
('prop.svc-hiveseq.action.10.0','2'),
('prop.svc-hiveseq.isPostponed.10.3','0'),
('prop.svc-hiveseq.reqPriority.10.7','0')
]

comand = urllib.urlencode(valuz)
print comand
response2 = opener.open(hive_URL, comand)
new_id = response2.read()
print new_id