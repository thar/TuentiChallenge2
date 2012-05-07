#!/usr/bin/python

#Autor: Miguel Angel Julian Aguilar
#e-mail: miguel.a.j82@gmail.com

import sys
from time import sleep

def find_gcf(dividend,divisor):
    reminder=-1
    while reminder !=0:
        qoutient=dividend/divisor
        reminder=dividend%divisor
        if reminder !=0:
            dividend=divisor
            divisor=reminder
    gcf=divisor
    return divisor

def find_lcm(x,y,gcf):
    lcm=(x*y)/gcf
    return lcm

lines=sys.stdin.readlines()
nCases=int(lines.pop(0).strip())

#lines=[]
#lines.append('100 50')

lineCount=1
for line in lines:
    lineData=line.strip().split()
    nCards=int(lineData[0])
    setCards=int(lineData[1])

    cards=range(nCards)
    cards2=cards

    indexChanges=[]

    i=0

    n1=nCards-2*min(setCards,nCards-setCards)
    if setCards<=nCards/2:
        p1=[]
        p2=[]
        for i in range(setCards):
            p1.append(-(nCards-2)+3*i)
        for i in range(n1):
            p1.append(p1[-1]+2)
        for i in range(setCards):
            p2.append((setCards-1)*2-3*i)
        p1.reverse()
        p1=p2+p1
    else:
        p1=[]
        p2=[]
        for i in range(n1):
            p1.append(nCards-1-2*i)
        for i in range(min(setCards,nCards-setCards)):
            p1.append(p1[-1]-3)
        for i in range(min(setCards,nCards-setCards)):
            p2.append(-(nCards-2)+3*i)
        p2.reverse()
        p1=p1+p2

    indexChanges=p1

    nChanges=[]
    rs=1

    #print 'comienzo la busqueda'

    checked=[]
    for i in range(nCards):
        nCh=0
        su=i
        while (su is not i and su not in checked) or nCh is 0:
            checked.append(su)
            nCh=nCh+1
            su=su+indexChanges[su]
            #print len(checked)
        if nCh>rs:
            dividend=nCh
            divisor=rs
        else:
            dividend=rs
            divisor=nCh
        #print 'i',
        gcf=find_gcf(dividend,divisor)
        rs=find_lcm(nCh,rs,gcf)
        #print 'o'
        #if i%100 is 0:
            #print i

    print 'Case #%d: %d' % (lineCount,rs)
    lineCount+=1
