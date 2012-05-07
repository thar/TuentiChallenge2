#!/usr/bin/python

#Autor: Miguel Angel Julian Aguilar
#e-mail: miguel.a.j82@gmail.com


import sys
import decimal
import time
from time import mktime
from datetime import datetime

#Leds que se encienden en el paso del anterior numero al nuevo
diferencias={}
diferencias['90']=1
diferencias['01']=0
diferencias['12']=4
diferencias['23']=1
diferencias['34']=1
diferencias['45']=2
diferencias['56']=1
diferencias['67']=1
diferencias['78']=4
diferencias['89']=0
diferencias['50']=2
diferencias['20']=2
diferencias['30']=2

encendidos={}
encendidos['0']=6
encendidos['1']=2
encendidos['2']=5
encendidos['3']=5
encendidos['4']=4
encendidos['5']=5
encendidos['6']=6
encendidos['7']=3
encendidos['8']=7
encendidos['9']=6

def numero_a_digitos(numero):
    cadena=''
    horas=int(numero/3600.0)
    numero=numero-horas*3600
    horas=horas%24
    if horas<10:
        cadena+='0'
    cadena+=str(horas)
    minutos=int(numero/60.0)
    if minutos<10:
        cadena+='0'
    cadena+=str(minutos)
    numero=numero-minutos*60
    segundos=numero
    if segundos<10:
        cadena+='0'
    cadena+=str(segundos)
    return cadena

def get_cambios_delta_clock(cadena_nueva,cadena_vieja):
    cambios=0
    for i in range(len(cadena_nueva)):
        if cadena_nueva[i]!=cadena_vieja[i]:
            cambios+=diferencias[cadena_vieja[i]+cadena_nueva[i]]
    return cambios

def get_cambios_old_clock(cadena):
    cambios=0
    for numero in cadena:
        cambios+=encendidos[numero]
    return cambios

ineficienciaDiaria=2255477

for line in sys.stdin:
    line=line.strip()
    t1=line[:len(line)/2].strip()
    t2=line[len(line)/2+1:].strip()

    ts1=time.strptime(t1,"%Y-%m-%d %H:%M:%S")
    ts2=time.strptime(t2,"%Y-%m-%d %H:%M:%S")    

    dt1 = datetime.fromtimestamp(mktime(ts1))
    dt2 = datetime.fromtimestamp(mktime(ts2))

    diffTime=dt2-dt1
    days=diffTime.days
    secs=diffTime.seconds

    origSec=ts1.tm_sec+60*ts1.tm_min+60*60*ts1.tm_hour
    origCadena=numero_a_digitos(origSec)
    startChanges=get_cambios_old_clock(origCadena)

    cambiosOldClock=0
    cambiosDeltaClock=startChanges
    cadena_vieja=origCadena
    for i in range(origSec,origSec+secs+1):
        cambiosOldClock+=get_cambios_old_clock(numero_a_digitos(i))
        cadena_nueva=numero_a_digitos(i)
        cambiosDeltaClock+=get_cambios_delta_clock(cadena_nueva,cadena_vieja)
        cadena_vieja=cadena_nueva        

    print cambiosOldClock-cambiosDeltaClock+days*ineficienciaDiaria


