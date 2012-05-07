#!/usr/bin/python

#Autor: Miguel Angel Julian Aguilar
#e-mail: miguel.a.j82@gmail.com

import sys
from hashlib import md5
import re

content=[]
for i in range(1,801):
    f=open('/home/maps/documents/%04d' % i)
    content.append(f.read().lower())
    f.close()

lines=sys.stdin.readlines()

nCases=int(lines.pop(0).strip())


for line in lines:
    inData=line.strip().split()
    word=inData[0]
    limi=int(inData[1])
    
    p = re.compile(r'\b%s\b' % word)

    i=0
    found=0
    fichero=0
    lastFileFound=0

    for i in range(800):
        fileFound=len(p.findall(content[i]))
        found=found+fileFound
        if found>=limi:
            fichero=i
            break
        lastFileFound=found

    iterator = p.finditer(content[fichero])
    for i in range(limi-lastFileFound-1):
        iterator.next()

    fin=iterator.next().span()[1]
    data=content[fichero][:fin]
    fila=data.count('\n')+1
    lastCarrRet=data.rfind('\n')
    data=data[lastCarrRet+1:]
    
    words=data.split()
    print '%d-%d-%d' % (fichero+1,fila,len(words))


