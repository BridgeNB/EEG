__author__ = 'zhengyangqiao'

import io
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read raw data input
# rawData = np.genfromtxt("rawData_without_header.csv", delimiter=',')
rawData = pd.read_csv("Raw-Diff-Class-Condensed.csv", delimiter=',')

## split raw data by object name - convert to a func!]

BB = rawData[rawData['Code'][:] == "BB"]

# initiate variables
iniAction = BB['Action'][0]
print(iniAction)

# count the different action numbers -- convert to a func!!!
actionCount = 0

for actionIndex in range(1,len(BB)):
    if BB['Action'][actionIndex] != iniAction:
        actionCount = actionCount + 1
        iniAction = BB['Action'][actionIndex]

print "Different Action Count " + str(actionCount)


## split data by action and store it by attributes

# initiate the attributes title need to add one!!!
actionAttributes = [i for i in range(actionCount + 1)]

# initiate action dictionary
actionWareHouse = {}
for actionAttribute in actionAttributes:
    actionWareHouse[actionAttribute] = []

print actionAttributes
# store value to action dictionary
iniAction = BB['Action'][0]
attribute = 0

print "iniAction " + str(iniAction);
for actionIndex in range(1,len(BB)) :

    if int(BB['Action'][actionIndex]) == int(iniAction):
        actionWareHouse[attribute].append(BB.iloc[actionIndex])
    else:
        print "actionAttrbute " + str(attribute)
        attribute = attribute + 1
        iniAction =BB['Action'][actionIndex]

print len(actionWareHouse[0])
print len(actionWareHouse[1])
print len(actionWareHouse[2])
print len(actionWareHouse[3])
print len(actionWareHouse[32])
print len(actionWareHouse[33])
print len(actionWareHouse[34])