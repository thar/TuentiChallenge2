#!/usr/bin/python

#Autor: Miguel Angel Julian Aguilar
#e-mail: miguel.a.j82@gmail.com

import sys
import string

class Key:
    def __init__(self,keys):
        self.keys=keys
    def pressToKey(self,key):
        if not key in self.keys: return 0
        else: return 1+self.keys.index(key)

keys={}
keys[1]=Key([' ','1'])
keys[2]=Key(['a','b','c','2'])
keys[3]=Key(['d','e','f','3'])
keys[4]=Key(['g','h','i','4'])
keys[5]=Key(['j','k','l','5'])
keys[6]=Key(['m','n','o','6'])
keys[7]=Key(['p','q','r','s','7'])
keys[8]=Key(['t','u','v','8'])
keys[9]=Key(['w','x','y','z','9'])
keys[0]=Key(['0'])
keys['may']=Key(['may'])

charToKey={}
charToKey['0']=0
charToKey['1']=1
charToKey['2']=2
charToKey['3']=3
charToKey['4']=4
charToKey['5']=5
charToKey['6']=6
charToKey['7']=7
charToKey['8']=8
charToKey['9']=9
charToKey[' ']=1
charToKey['a']=2
charToKey['b']=2
charToKey['c']=2
charToKey['d']=3
charToKey['e']=3
charToKey['f']=3
charToKey['g']=4
charToKey['h']=4
charToKey['i']=4
charToKey['j']=5
charToKey['k']=5
charToKey['l']=5
charToKey['m']=6
charToKey['n']=6
charToKey['o']=6
charToKey['p']=7
charToKey['q']=7
charToKey['r']=7
charToKey['s']=7
charToKey['t']=8
charToKey['u']=8
charToKey['v']=8
charToKey['w']=9
charToKey['x']=9
charToKey['y']=9
charToKey['x']=9
charToKey['may']='may'

keysToRowCol={}
keysToRowCol[1]={'c':0, 'r':0}
keysToRowCol[2]={'c':1, 'r':0}
keysToRowCol[3]={'c':2, 'r':0}
keysToRowCol[4]={'c':0, 'r':1}
keysToRowCol[5]={'c':1, 'r':1}
keysToRowCol[6]={'c':2, 'r':1}
keysToRowCol[7]={'c':0, 'r':2}
keysToRowCol[8]={'c':1, 'r':2}
keysToRowCol[9]={'c':2, 'r':2}
keysToRowCol[0]={'c':1, 'r':3}
keysToRowCol['may']={'c':2, 'r':3}

def movesFromKeyToKey(start,end):
    global keysToRowCol
    diffCols=abs(keysToRowCol[start]['c']-keysToRowCol[end]['c'])
    diffRows=abs(keysToRowCol[start]['r']-keysToRowCol[end]['r'])
    diag=min(diffCols,diffRows)
    vert=diffRows-diag
    horiz=diffCols-diag
    return [horiz,vert,diag]

timeVert=300
timeHori=200
timeDiag=350
timePres=100
timeSame=500

lineCount=0
for line in sys.stdin:
    if lineCount is 0:
        lineCount=1
        continue
    actual_key=0
    capsLoc=False
    changeCapsLoc=False
    horiz=0
    vert=0
    diag=0
    pulses=0
    sameKeyWait=0
    for char in line:
        if charToKey.has_key(char.lower()):
            k=charToKey[char.lower()]
            if char in string.ascii_lowercase and capsLoc:
                changeCapsLoc=True
            elif char in string.ascii_uppercase and not capsLoc:
                changeCapsLoc=True
            else:
                changeCapsLoc=False
            char=char.lower()
            if(changeCapsLoc):
                moves=movesFromKeyToKey(actual_key,'may')
                horiz=horiz+moves[0]
                vert=vert+moves[1]
                diag=diag+moves[2]
                pulses=pulses+1
                actual_key='may'
                capsLoc=not capsLoc
            if actual_key==k:
                sameKeyWait=sameKeyWait+1
            else:
                moves=movesFromKeyToKey(actual_key,k)
                horiz=horiz+moves[0]
                vert=vert+moves[1]
                diag=diag+moves[2]
                actual_key=k
            pulses=pulses+keys[k].pressToKey(char)
    print horiz*timeHori+vert*timeVert+diag*timeDiag+pulses*timePres+sameKeyWait*timeSame




