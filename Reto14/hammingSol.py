#!/usr/bin/python

#Autor: Miguel Angel Julian Aguilar
#e-mail: miguel.a.j82@gmail.com

import sys

lines=sys.stdin.readlines()

def binary(n, digits=8):
    return [int(x) for x in list("{0:0>{1}}".format(bin(n)[2:], digits))]

def generateHamming(num):
    b=binary(num,4)
    dataParity=[]
    dataParity.append((b[0]+b[1]+b[3])%2)
    dataParity.append((b[0]+b[2]+b[3])%2)
    dataParity.append((b[1]+b[2]+b[3])%2)
    hamData=[dataParity[0],dataParity[1],b[0],dataParity[2],b[1],b[2],b[3]]
    return hamData

hammini=[]
for i in range(16):
    hammini.append(generateHamming(i))

def getDistance(a,b):
    dist=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            dist+=1
    return dist

def fixHam(data):
    di=7
    fixData=[]
    for i in range(16):
        nDi=getDistance(data,hammini[i])
        if nDi<di:
            di=nDi
            fixData=hammini[i]
    return fixData

for line in lines:
    lineData=list(line.strip())
    if len(lineData)%7!=0:
        print 'Error!'
        continue
    nDatos=len(lineData)/7
    datos=[]
    newData=[]
    for i in range(nDatos):
        datos.append([int(x) for x in lineData[i*7:(i+1)*7]])
        newData.append(hammini.index(fixHam(datos[-1])))
    
    outData=''
    for i in range(0,len(newData),2):
        outData+=chr((newData[i]<<4)+newData[i+1])
    error=False
    for char in outData:
        if ord(char) not in range(32,127):
            print 'Error!'
            error=True
            break
    if not error:
        print outData


