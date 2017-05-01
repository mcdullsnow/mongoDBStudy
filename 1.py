import os
import csv
import pprint

DATADIR='/Users/huixueshao/Downloads/data_analysis'
DATAFILE='beatles-diskography.csv'

def parse_data(datafile):
    data = []
    with open(datafile,'r') as df:
        r = csv.DictReader(df)
        for each_line in r:
            data.append(each_line)
    return data

if __name__ == "__main__":
    datafile = os.path.join(DATADIR,DATAFILE)
    parse_data(datafile)
    d = parse_data(datafile)
    pprint.pprint(d)
