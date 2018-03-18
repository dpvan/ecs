# -*- coding:UTF-8 -*-
import sys
import os
import datetime
uuids = []
flavorNames = []
createTimes = []
with open('./TrainData_2015.1.1_2015.2.19.txt', 'r') as fp:
    array = []
    for line1 in fp:
        array.append(line1)
for item in array:
    	values = item.split("\t")
    	uuid = values[0]
    	flavorName = values[1]
    	createTime = values[2]
    	uuids.append(uuid)
    	flavorNames.append(flavorName)
    	createTimes.append(createTime)
        dateValue1 = createTime.split(' ')
        createdate1 = dateValue1[0]
        dateValue2 = createTimes[0].split(' ')
        createdate2 = dateValue2[0]
        d2 = datetime.datetime.strptime(createdate2, '%Y-%m-%d')
        d1 = datetime.datetime.strptime(createdate1, '%Y-%m-%d')
        delta1 = d1 - d2

        # if delta1.days<1:
        #     print flavorNames
        if delta1.days>1:
            print flavorNames

print flavorNames.count('flavor15')
