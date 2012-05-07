#!/usr/bin/python

#Autor: Miguel Angel Julian Aguilar
#e-mail: miguel.a.j82@gmail.com

import sys

lines=sys.stdin.readlines()

try:
    numero_de_casos=int(lines.pop(0).strip())
except:
    print 'Error: No se pudieron obtener el numero de casos'
    exit()

for caso in range(numero_de_casos):
    #try:
        pista=lines.pop(0).strip()
        #print pista
        grupos=lines.pop(0).strip()
        pistaDatos=pista.split()
        grupos=grupos.split()
        races=int(pistaDatos[0])
        karts=int(pistaDatos[1])
        groupsN=int(pistaDatos[2])
        litros=0
        gruposEnCarrera=[]
        
        #gruposDeCarrera=[int(grupos[0])]
        gruposDeCarrera=[0]
        #indice=1%groupsN
        indice=0
        #freeKarts=karts-gruposDeCarrera[0]
        freeKarts=karts
        #gruposAdded=1
        gruposAdded=0
        freeKarts1=[]
        indicesCarrerasIndex0=[]

        while len(gruposDeCarrera)<=races:
            #print freeKarts
            if indice==0:
                #print 'karts libres: ',freeKarts,' carreras: ',len(gruposDeCarrera)
                if freeKarts in freeKarts1:
                    #print 'fin por subconjunto encontrado'
                    #print 'bucle'
                    #print 'indice de aparicion en el bucle:',freeKarts1.index(freeKarts)
                    #print 'tengo',len(gruposDeCarrera),'carreras diferentes'
                    racesBeforeLoop=indicesCarrerasIndex0[freeKarts1.index(freeKarts)]
                    if freeKarts is not 0:
                        racesBeforeLoop=racesBeforeLoop-1
                        gruposDeCarrera.pop(-1)
                    #print 'llevaba',racesBeforeLoop,'antes del bucle'
                    loopSize=len(gruposDeCarrera)-racesBeforeLoop
                    loopRaces=gruposDeCarrera[(len(gruposDeCarrera)-loopSize):]
                    #print 'me quedo con un conjunto de',loopSize,'carreras'
                    #print 'numero de veces que se repite el subconjunto: ',(races-racesBeforeLoop)/loopSize
                    #print 'carreras que faltan: ',(races-racesBeforeLoop)%loopSize
                    #print 'karts:',freeKarts,'lista freeKarts:',freeKarts1,'indice:',indicesCarrerasIndex0,'loop:',loopRaces,'carreras:',gruposDeCarrera
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
                    #print 'fin por conjunto encontrado'
                    #print 'tengo',len(gruposDeCarrera),'carreras diferentes'
                    #print 'numero de veces que se repite el conjunto: ',races/len(gruposDeCarrera)
                    #print 'carreras que faltan: ',races%len(gruposDeCarrera)
                    #print 'litros del grupo:',sum(gruposDeCarrera)
                    litros=(races/len(gruposDeCarrera))*sum(gruposDeCarrera)+sum(gruposDeCarrera[0:races%len(gruposDeCarrera)])
                    #print 'litros totales:',litros
                    break
                gruposDeCarrera.append(int(grupos[indice]))
                freeKarts=karts-int(grupos[indice])
                gruposAdded=0
            indice=(indice+1)%groupsN
            gruposAdded=gruposAdded+1
            #print indice,gruposDeCarrera[-1],len(gruposDeCarrera)
        if len(gruposDeCarrera)>races:
            #print 'fin por limite de carreras'
            litros=sum(gruposDeCarrera[:races])

        print litros
    #except Exception, e:
        #print e



