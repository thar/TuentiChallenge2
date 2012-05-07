#!/usr/bin/python

#Autor: Miguel Angel Julian Aguilar
#e-mail: miguel.a.j82@gmail.com

import sys

def binToDec(binstr):
    decnum = 0
    for i in binstr:
        decnum = decnum * 2 + int(i)
    return decnum

lineCount=0
for line in sys.stdin:
    if lineCount is 0:
        lineCount=1
        continue
    line=line.strip()
    number=None
    try:
        number=int(line)
    except Exception:
        pass
    if not number:
        print 'Case #%d: Error' % (lineCount)
    elif number<2:
        print 'Case #%d: %d' % (lineCount,number)
    else:
        binaryForm=bin(number)[2:]
        maxNumberOfOnes=0
        carrier=False
        binNumero1=''
        binNumero2=''
        for i in range(len(binaryForm)-1,-1,-1):
            if i==0:
                if not carrier:
                    maxNumberOfOnes=maxNumberOfOnes+1
                    binNumero1='1'+binNumero1
                    binNumero2='0'+binNumero2
                continue
            if binaryForm[i]=='0':
                if carrier:
                    maxNumberOfOnes=maxNumberOfOnes+1
                    carrier=True
                    binNumero1='1'+binNumero1
                    binNumero2='0'+binNumero2
                else:
                    maxNumberOfOnes=maxNumberOfOnes+2
                    carrier=True
                    binNumero1='1'+binNumero1
                    binNumero2='1'+binNumero2
            else:
                if carrier:
                    maxNumberOfOnes=maxNumberOfOnes+2
                    binNumero1='1'+binNumero1
                    binNumero2='1'+binNumero2
                else:
                    maxNumberOfOnes=maxNumberOfOnes+1
                    binNumero1='1'+binNumero1
                    binNumero2='0'+binNumero2

        print 'Case #%d: %d' % (lineCount,maxNumberOfOnes)
        numero1=binToDec(binNumero1)
        numero2=binToDec(binNumero2)
        #print numero1,binNumero1,numero2,binNumero2,numero1+numero2,bin(numero1+numero2)[2:],number,binaryForm
    lineCount=lineCount+1


