import os
import pprint
import csv

DATADIR=""
DATAFILE="#csv文件名"

def pasre_csv(datafile):
    data = []
    n = 0
    with open(datafile,'rb') as sd:
        r = csv.DictReader(sd)
        for line in r:
            data.append(line)
    return data

if __name__=='__main__':
    datafile = os.path.join(DATADIR,DATAFILE)
    pasre_csv(datafile)
    d=pasre_csv(datafile)
    pprint.pprint(d)


