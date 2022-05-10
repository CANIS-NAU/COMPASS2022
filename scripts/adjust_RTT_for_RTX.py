import csv
import sys

delays_file = sys.argv[1]
rtx_file = sys.argv[2]
distance = sys.argv[3]
'''
test name:  LOS_Outdoor_10m
tests run:  250
test start: 07 Aug, 2021 17:57:57 UTC
test end:   07 Aug, 2021 18:16:08 UTC

retransmissions: 2 tests - [4, 197]

ESP1->GWYB: 1304.144ms
GWYB->GWYA: 294.908ms
GWYA->ESP2: 1582.248ms
RTT       : 3181.3ms
'''
'''
Test, ESP1, GWYB, GWYA, ESP2
'''

rtx_tests={}

with open(rtx_file, "r") as fi:
    lines=fi.readlines()
    for line in lines:
        if "retransmissions:" in line:
            line.strip()
            rtx = line.split("[")[-1].strip().replace("]","").split(", ")
            for t in rtx:
                if t not in rtx_tests:
                    rtx_tests[t]=0
                rtx_tests[t]+=1

with open(delays_file, "r") as fi:
    rows=csv.reader(fi, delimiter=",")
    count=0
    for row in rows:
        if count == 0:
            count+=1
            continue
        test=row[0]
        print(row)
        # Check to see if the test was RTX'd
        RTT=0
        if test in rtx_tests:
            if rtx_tests[test] > 0:
                RTT=int(row[4].strip())-int(row[1].strip()) + (rtx_tests[test]*20000)

        else:
            rtx_tests[test]=0
            RTT=int(row[4].strip())-int(row[1].strip())
        with open("adjusted_rtt.csv", "a") as fo:
            fo.write("%s,%s,%s,%s\n" % (distance, test, RTT, rtx_tests[test]))



