# -*- coding:UTF-8 -*-
import sys
import os
def generate_index(n, step=2): #数据切割函数
    for i in range(0, n, step):
        yield (i, i + step) if i + step < n else (i, None)
with open('./TrainData_2015.1.1_2015.2.19.txt', 'r') as fp:
	array = []
	for line1 in fp:
		dss11=line1[-20:-1]
		dss1=line1[:13]
		array.append(dss1)
	print array
	for i, j in generate_index(len(array)):
	    print(tuple(array[i: j]))
fp=open('./TrainData_2015.1.1_2015.2.19.txt','r')
array2 = []
for line2 in fp:
	dss2=line2[14:-21]
	array2.append(dss2)
print array2
i = 1
while i<=22:
	if array2.count('flavor%d'%i)!=0:
		print u'flavor%d个数为'%i
		print array2.count('flavor%d'%i)
	i = i+1
fp.close()
fp=open('./TrainData_2015.1.1_2015.2.19.txt','r')
array3 = []
for line3 in fp:
	dss3=line3[-20:-1]
	array3.append(dss3)
print array3
fp.close()
