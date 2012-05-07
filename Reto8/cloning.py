#!/usr/bin/python

#Autor: Miguel Angel Julian Aguilar
#e-mail: miguel.a.j82@gmail.com

#Ni un minuto en completar el test

import sys
from hashlib import md5

lines=sys.stdin.readlines()

q=lines.pop(0).strip().decode('utf-8')

line=lines.pop().strip().decode('utf-8')
clonRulesTemp=line.split(',')
clonRules={}
for i in range(len(clonRulesTemp)):
    t=clonRulesTemp[i].split('=>')
    clonRules[t[0]]=t[1]
idx=1
while len(lines)>0:
    line=lines.pop().strip().decode('utf-8')
    clonRulesTemp=line.split(',')
    clonRulesN={}
    for i in range(len(clonRulesTemp)):
        t=clonRulesTemp[i].split('=>')
        tt1=list(t[1])
        for i in range(len(tt1)):
            if clonRules.has_key(tt1[i]):
                tt1[i]=clonRules[tt1[i]]
        t[1]=''.join(tt1)
        clonRulesN[t[0]]=t[1]
        for key in clonRules.keys():
            if not clonRulesN.has_key(key):
                clonRulesN[key]=clonRules[key]
    clonRules=clonRulesN
    idx=idx+1

m=md5()
q=list(q)
for i in range(len(q)):
    if clonRules.has_key(q[i]):
        q[i]=clonRules[q[i]]
    m.update(q[i])
q=[]
print m.hexdigest()