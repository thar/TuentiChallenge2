#!/usr/bin/python

#Autor: Miguel Angel Julian Aguilar
#e-mail: miguel.a.j82@gmail.com

import sys
import cmath
from cmath import pi as pi

# determine if a point is inside a given polygon or not
# Polygon is a list of (x,y) pairs.
def point_inside_polygon(x,y,poly):
    n = len(poly)
    inside =False
    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x,p1y = p2x,p2y
    return inside

def cart2polar(x,y):
    c=complex(x,y)
    p=cmath.polar(c)
    return [p[0],p[1]]

def polar2cart(x,y):
    c=cmath.rect(x,y)
    return [c.real,c.imag]
    

class Ingredient:
    #Inicializacion del ingrediente. Vertices, centro, angulos desde el centro de la pizza hasta sus vertices, etc...
    def __init__(self,ingName,nVerts,centerX,centerY,v1X,v1Y):
        self.ingName=ingName
        anglePass=2.*pi/nVerts
        v1Xt=v1X-centerX
        v1Yt=v1Y-centerY
        verts=[]
        v1Pol=cart2polar(v1Xt,v1Yt)
        self.centerPolar=cart2polar(centerX,centerY)
        self.radious=v1Pol[0]
        self.minAngle=2*pi
        self.maxAngle=-2*pi
        self.minRad=v1Pol[0]
        self.maxRad=v1Pol[0]
        for i in range(nVerts):
            verts.append(polar2cart(v1Pol[0],v1Pol[1]+i*anglePass))
        for i in range(nVerts):
            verts[i]=[verts[i][0]+centerX,verts[i][1]+centerY]
        self.inCenter=point_inside_polygon(0.,0.,verts)
        for i in range(nVerts):
            verts[i]=cart2polar(verts[i][0],verts[i][1])
            if verts[i][1]<self.minAngle:
                self.minAngle=verts[i][1]
            if verts[i][1]>self.maxAngle:
                self.maxAngle=verts[i][1]
            if verts[i][0]<self.minRad:
                self.minRad=verts[i][0]
            if verts[i][0]>self.maxRad:
                self.maxRad=verts[i][0]

    #parte un rango de posibles cortes en rangos que no corten al ingrediente
    def split(self,grp):
        if self.inCenter:
            return []
        newGrp=[]
        maxAngle=self.maxAngle*180/pi if self.maxAngle>=0 else (self.maxAngle+pi)*180/pi
        minAngle=self.minAngle*180/pi if self.minAngle>=0 else (self.minAngle+pi)*180/pi
        if minAngle<maxAngle:
            for g in grp:
                if g[0]<minAngle:
                    newGr=[g[0],min(minAngle,g[1])]
                    if newGr[0]<newGr[1] and newGr not in newGrp:
                        newGrp.append(newGr)
                if g[1]>maxAngle:
                    newGr=[max(maxAngle,g[0]),g[1]]
                    if newGr[0]<newGr[1] and newGr not in newGrp:
                        newGrp.append(newGr)
        else:
            for g in grp:
                if g[0]<maxAngle and g[1]>maxAngle:
                    newGr=[maxAngle,min(minAngle,g[1])]
                    if newGr[0]<newGr[1] and newGr not in newGrp:
                        newGrp.append(newGr)
                if g[0]<minAngle:
                    newGr=[max(g[0],maxAngle),min(minAngle,g[1])]
                    if newGr[0]<newGr[1] and newGr not in newGrp:
                        newGrp.append(newGr)
        return newGrp

    #Dado un rango de corte, determina en que lado queda el ingrediente
    def checkIngZone(self,grp):
        sign=1
        if self.centerPolar[1]<0:
            sign=-1
        cent=self.centerPolar[1]*180/pi if self.centerPolar[1]>=0 else (self.centerPolar[1]+pi)*180/pi
        if cent<grp[0]:
            return sign
        else:
            return -sign

lines=sys.stdin.readlines()

nPizzas=int(lines.pop(0).strip())

for i in range(nPizzas):
    pizzaGeom=[float(x) for x in lines.pop(0).strip().split()]
    pizzaCenter=pizzaGeom[:2]
    pizzaRad=pizzaGeom[2]
    pizzaIng=int(lines.pop(0).strip())
    splitsGrp=[[0,180]]
    for j in range(pizzaIng):
        ingredientData=lines.pop(0).strip().split()
        ingName=ingredientData[0]
        nVertIng=int(ingredientData[1])
        nIng=int(ingredientData[2])
        ings=[]
        for k in range(nIng):
            ingDat=[float(x) for x in lines.pop(0).strip().split()]
            ing=Ingredient(ingName,nVertIng,ingDat[0]-pizzaCenter[0],ingDat[1]-pizzaCenter[1],ingDat[2]-pizzaCenter[0],ingDat[3]-pizzaCenter[1])
            ings.append(ing)
        #Ya tengo las piezas del ingrediente. Ahora tengo que buscar los posibles cortes de la pizza que no cortan ninguna pieza
        for ing in ings:
            splitsGrp=ing.split(splitsGrp)
        #Me quedo con los cortes que dejen un mismo numero de ingredientes en un lado y en el otro
        newSplGrp=[]
        for gr in splitsGrp:
            grpPoints=0
            for ing in ings:
                grpPoints+=ing.checkIngZone(gr)
            if grpPoints==0:
                newSplGrp.append(gr)
        splitsGrp=newSplGrp

    if len(splitsGrp)>0:
        print 'Case #%d: TRUE' % (i+1)
    else:
        print 'Case #%d: FALSE' % (i+1)


