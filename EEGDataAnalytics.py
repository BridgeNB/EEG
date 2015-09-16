__author__ = 'zhengyangqiao'


import io
import csv
import numpy as np

def read_csv(filename):
    # Open file in filename
    f = open(filename, 'rU')
    reader = csv.reader(f, delimiter=',', skipinitialspace=True)
    # Find the header
    headers = reader.next()
    print headers

    column = {}

    for h in headers:
        column[h] = []

    for row in reader:
        for h, v in zip(headers, row):
            column[h].append(v)

    print column['Code'][0:2]
    print column['Group'][0:2]
    print column['AveWorkload'][0:2]

read_csv('Raw-Diff-Class-Condensed.csv')

#
# CVSimport()