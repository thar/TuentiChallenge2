#!/usr/bin/python

#Autor: Miguel Angel Julian Aguilar
#e-mail: miguel.a.j82@gmail.com

import sys
from math import ceil, floor

def getAvg(fontSizePx,ct):
    result=(floor(fontSizePx)**2.0)/(2.0*ct)
    return result

lines=sys.stdin.readlines()

try:
    numero_de_casos=int(lines.pop(0).strip())
except:
    print 'Error: No se pudieron obtener el numero de casos'
    exit()

lineCount=1
for caso in range(numero_de_casos):
    datos=lines.pop(0).strip()
    datos=datos.split()
    W=1.0*int(datos[0])
    H=1.0*int(datos[1])
    ct=1.0*int(datos[2])
    nPixW=W*ct
    nPixH=H*ct
    frase=lines.pop(0).strip()
    palabras=frase.split()
    nPalabras=len(palabras)
    nChars=1.0*len(frase)
    nCharsNoSpace=nChars-frase.count(' ')
    maxPix=-1
    pix=0
    nLines=0
    while pix>maxPix or pix==0:
        nLines=nLines+1
        maxPix=pix
        lineString=['']
        nCharsW=0
        for palabra in palabras:
            charsToSplit=nChars/nLines-len(lineString[-1])-(nLines-1)
            if len(lineString[-1])==0 or charsToSplit>0:
                lineString[-1]=lineString[-1]+' '+palabra.strip()
                lineString[-1]=lineString[-1].strip()
            else:
                lineString.append(palabra)
            nCharsWn=len(lineString[-1])
            if nCharsWn>nCharsW:
                nCharsW=nCharsWn

        maxFontSizeW=nPixW/nCharsW
        maxFontSizeH=nPixH/len(lineString)
        pix=min(maxFontSizeW,maxFontSizeH)

    le=nCharsNoSpace*getAvg(maxPix,ct)
    print 'Case #%d: %d' % (lineCount,ceil(le))
    lineCount=lineCount+1
