#! /bin/bash

'''
Requested by collaborators. From the phased mutation table generated in the DRM pipeline, this shell script maps the gag-pol coordinate and AA changes from WT to Sub into the protease, RTase, and integrase regions.
'''

input_file="DRMtable.csv"
output_file="DRMoutput.csv"
AAPOS="3"
AAREF="5"
AASUB="6"

awk -F',' 'BEGIN {
    print "AAREF" "," "AAPOS" "," "AASUB" "," "CDS" 
}
NR > 1 {
    if ($'$AAPOS' >= 489 && $'$AAPOS' <= 587){print $'$AAREF' "," $'$AAPOS' - 488 "," $'$AASUB' "," "NP_705926.1"}
    else if ($'$AAPOS' >= 588 && $'$AAPOS' <= 1147){print $'$AAREF' "," $'$AAPOS' - 587 "," $'$AASUB' "," "NP_705927.1"} 
    else if ($'$AAPOS' >= 1148 && $'$AAPOS' <= 1435){print $'$AAREF' "," $'$AAPOS' - 1147 "," $'$AASUB' "," "NP_705928.1"}
}' "$input_file" > "$output_file"