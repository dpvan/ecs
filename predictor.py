# -*- coding:UTF-8 -*-
import sys
import os
import datetime
import time
def generate_index(n, step=2): #数据切割函数
    for i in range(0, n, step):
        yield (i, i + step) if i + step < n else (i, None)
uuids = []
flavorNames = []
createTimes = []
with open('./TrainData_2015.1.1_2015.2.19.txt', 'r') as fp:
	 	array = []
		for line1 in fp:
			# dss11=line1[-20:-1]
			# dss1=line1[:13]
			array.append(line1)
for  item in array:
        values = item.split("\t")
        uuid = values[0]
        flavorName = values[1]
        createTime = values[2]
	uuids.append(uuid)
	flavorNames.append(flavorName)
	createTimes.append(createTime)
# print uuids
str = '2012-11-19'
str2 = '2012-11-20'
date_time1 = datetime.datetime.strptime(str,'%Y-%m-%d')
date_time2 = datetime.datetime.strptime(str2,'%Y-%m-%d')
print date_time2-date_time1
