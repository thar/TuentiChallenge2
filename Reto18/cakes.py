#!/usr/bin/python

#Autor: Miguel Angel Julian Aguilar
#e-mail: miguel.a.j82@gmail.com

import sys

lines=sys.stdin.readlines()

nCases=int(lines.pop(0).strip())

for i in range(nCases):
    nCuts=int(lines.pop(0).strip())
    print 'Case #%d: %d' % (i+1,1+sum(range(nCuts+1)))
