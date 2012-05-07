#!/usr/bin/python

#Autor: Miguel Angel Julian Aguilar
#e-mail: miguel.a.j82@gmail.com

import sys

start=0
end=0
maxGap=0
stockValues=[]
for line in sys.stdin:
    line=line.strip()
    number=None
    try:
        number=int(line)
    except Exception:
        pass
    if not number:
        continue
    stockValues.append(number)

minV=stockValues[0]
maxV=minV
gap=0
minI=0
maxI=0

for i in range(len(stockValues)):
    if stockValues[i]<minV:
        minV=stockValues[i]
        minI=i
        maxV=stockValues[i]
        maxI=i
        gap=maxV-minV
    if stockValues[i]>maxV:
        maxV=stockValues[i]
        maxI=i
        gap=maxV-minV
        if gap>maxGap:
            start=minI
            end=maxI
            maxGap=gap

print 100*start,100*end,maxGap

