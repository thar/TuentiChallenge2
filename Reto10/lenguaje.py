#!/usr/bin/python

#Autor: Miguel Angel Julian Aguilar
#e-mail: miguel.a.j82@gmail.com


import sys

for line in sys.stdin:
    numbers=[]
    elements_chars = line.strip().split()
    for element in elements_chars:
        try:
            n=int(element)
            numbers.append(n)
        except Exception, e:
            if element=='@':
                lastNum=numbers.pop()
                antLasNum=numbers.pop()
                numbers.append(lastNum+antLasNum)
            elif element=='$':
                lastNum=numbers.pop()
                antLasNum=numbers.pop()
                numbers.append(antLasNum-lastNum)
            elif element=='&':
                lastNum=numbers.pop()
                antLasNum=numbers.pop()
                numbers.append(antLasNum/lastNum)
            elif element=='#':
                lastNum=numbers.pop()
                antLasNum=numbers.pop()
                numbers.append(antLasNum*lastNum)
            elif element=='mirror':
                lastNum=numbers.pop()
                numbers.append(-lastNum)
            elif element=='dance':
                lastNum=numbers.pop()
                antLasNum=numbers.pop()
                numbers.append(lastNum)
                numbers.append(antLasNum)
            elif element=='fire':
                lastNum=numbers.pop()
            elif element=='breadandfish':
                numbers.append(numbers[-1])
            elif element=='conquer':
                lastNum=numbers.pop()
                antLasNum=numbers.pop()
                numbers.append(antLasNum%lastNum)
            elif element=='.':
                print numbers[-1]




