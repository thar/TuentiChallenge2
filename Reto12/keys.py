#!/usr/bin/python

#Autor: Miguel Angel Julian Aguilar
#e-mail: miguel.a.j82@gmail.com

import sys
#from PIL import Image

key1='a541714a17804ac281e6ddda5b707952'
key2='62cd275989e78ee56a81f0265a87562e'
key3='ed8ce15da9b7b5e2ee70634cc235e363'


#im = Image.open("CANTTF.png")

#d=im.tostring()

#i=0
#e=0
#
#for c in d:
#    i=i+1
#    e=(e << 1)+(ord(c) & 1)
#    if i==8:
#        print chr(e),
#        e=0
#        i=0

for line in sys.stdin:
    inData=line.strip()
    ou=''
    for i in range(32):
        s=int(key1[i], 16)+int(key2[i], 16)+int(key3[i], 16)+int(inData[i], 16)
        s=s%16
        ou=ou+hex(s)[2]
    print ou

