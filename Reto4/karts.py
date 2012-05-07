#!/usr/bin/python

#Autor: Miguel Angel Julian Aguilar
#e-mail: miguel.a.j82@gmail.com

#Not so proud of this one

import sys

lines=sys.stdin.readlines()

try:
    numero_de_casos=int(lines.pop(0).strip())
except:
    print 'Error: No se pudieron obtener el numero de casos'
    exit()

for caso in range(numero_de_casos):
    pista=lines.pop(0).strip()
    grupos=lines.pop(0).strip()
    pistaDatos=pista.split()
    grupos=grupos.split()
    races=int(pistaDatos[0])
    karts=int(pistaDatos[1])
    groupsN=int(pistaDatos[2])
    litros=0
    gruposEnCarrera=[]
    
    gruposDeCarrera=[0]
    indice=0
    freeKarts=karts
    gruposAdded=0
    freeKarts1=[]
    indicesCarrerasIndex0=[]

    while len(gruposDeCarrera)<=races:
        if indice==0:
            if freeKarts in freeKarts1:
                racesBeforeLoop=indicesCarrerasIndex0[freeKarts1.index(freeKarts)]
                if freeKarts is not 0:
                    racesBeforeLoop=racesBeforeLoop-1
                    gruposDeCarrera.pop(-1)
                loopSize=len(gruposDeCarrera)-racesBeforeLoop
                loopRaces=gruposDeCarrera[(len(gruposDeCarrera)-loopSize):]
                litros=sum(gruposDeCarrera[:racesBeforeLoop])+((races-racesBeforeLoop)/loopSize)*sum(loopRaces)+sum(loopRaces[:(races-racesBeforeLoop)%loopSize])
                break
            else:
                freeKarts1.append(freeKarts)
                indicesCarrerasIndex0.append(len(gruposDeCarrera))
        if freeKarts>=int(grupos[indice]) and gruposAdded<groupsN:
            freeKarts=freeKarts-int(grupos[indice])
            gruposDeCarrera[-1]=gruposDeCarrera[-1]+int(grupos[indice])
        else:
            if indice==0:
                litros=(races/len(gruposDeCarrera))*sum(gruposDeCarrera)+sum(gruposDeCarrera[0:races%len(gruposDeCarrera)])
                break
            gruposDeCarrera.append(int(grupos[indice]))
            freeKarts=karts-int(grupos[indice])
            gruposAdded=0
        indice=(indice+1)%groupsN
        gruposAdded=gruposAdded+1

    if len(gruposDeCarrera)>races:
        litros=sum(gruposDeCarrera[:races])

    print litros



