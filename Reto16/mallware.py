#!/usr/bin/python

#Autor: Miguel Angel Julian Aguilar
#e-mail: miguel.a.j82@gmail.com

import sys
import numpy as np
import mlpy


lines=sys.stdin.readlines()

knownReports=int(lines.pop(0).strip())
testCases=int(lines.pop(0).strip())
nSysCalls=int(lines.pop(0).strip())

learnData=[]
learnClas=[]

for i in range(knownReports):
    rep=lines.pop(0).strip().split()
    learnData.append(tuple(int(x) for x in rep[1:]))
    learnClas.append(1 if rep[0]=='M' else -1)

x=np.array(learnData)
y=np.array(learnClas)
#svm = mlpy.Knn(k = 1) #Otra posibilidad
svm = mlpy.Svm()
svm.compute(x,y)

checkCases=[]
suma=0
for i in range(testCases):
    rep=lines.pop(0).strip().split()
    case=[int(x) for x in rep]
    if svm.predict(np.array(case))==1:
        suma+=sum(case)

print suma


