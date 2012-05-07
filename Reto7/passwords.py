#!/usr/bin/python

#Autor: Miguel Angel Julian Aguilar
#e-mail: miguel.a.j82@gmail.com

import sys
from itertools import permutations

lines=sys.stdin.readlines()
rules=[]

passwords=[]
letters=[]
actual=[]

def checkIfOk(passw):
    global rules
    for i in range(len(passw)):
        for j in range(i+1,len(passw)):
            l1=passw[i]
            l2=passw[j]
            for rule in rules:
                if l1 in rule and l2 in rule:
                    if rule.index(l1)>rule.index(l2):
                        return False
    return True

for i in range(len(lines)):
    lines[i]=lines[i].strip()
    rules.append(lines[i])
    for letter in lines[i]:
        if letter not in letters: letters.append(letter)
    if lines[i][0] not in actual: actual.append(lines[i][0])


prevOk=True
while len(letters)>0:
    if prevOk:
        passwords.append([])
    newOptions=[]
    for possibleN in actual:
        for line in lines:
            if possibleN in line and line.index(possibleN) is not 0:
                possibleN=None
                break
        if possibleN and possibleN not in passwords[-1] and possibleN not in newOptions: newOptions.append(possibleN)
    if len(newOptions)>1:
        prevOk=False
    else:
        prevOk=True
    #prevOk=True
    passwords[-1]=passwords[-1]+newOptions
    lettersToRemove=[]
    for letter in passwords[-1]:
        if letter in letters:
            lettersToRemove.append(letter)
            letters.remove(letter)
            if not prevOk:
                break
    actual=[]
    for i in range(len(lines)):
        if len(lines[i])>0 and lines[i][0] in lettersToRemove: lines[i]=lines[i][1:]
        if len(lines[i])>0 and lines[i][0] not in actual: actual.append(lines[i][0])

realPass=['']
realPassCopy=realPass
for i in range(len(passwords)):
    possibles=''.join(elem[0] for elem in passwords[i])
    newList=list(permutations(possibles))
    newListCopy=[]
    for l in newList:
        if checkIfOk(l):
            newListCopy.append(l)
    newList=newListCopy
    newList.sort()
    realPassCopy=[]
    for passw in realPass:
        for l in newList:
            realPassCopy.append(passw+''.join(elem[0] for elem in l))
    realPass=realPassCopy
for p in realPass:
    if checkIfOk(p):
        print p