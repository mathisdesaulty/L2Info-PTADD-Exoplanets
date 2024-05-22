#Noms de fichiers en minuscules
#noms de variables et fonctions doivent commencer par une minuscule puis chaque mots qui les compose par une majuscule
#noms de classes doivent commencer chaque mot qui les compose par une majuscule

import numpy as np
import pandas
import sklearn

from Point import Point
from GroupeDePoints import GroupeDePoints
from Planete import Planete,PlanetePredite
from OutilsAnalyse import OutilsAnalyse

p1=Point("a",-1,1)
p2=Point("b",3,5)
p3=Point("c",0,2)
p4=Point("d",4,4)
l=[p1,p2,p3,p4]

print("Coordonnée X :",p1.getX())
grp=GroupeDePoints("grp",l)
print("Nombre de points dans le groupe :",grp.getNbPoints())
print("Centre :",grp.getCentre())

planete1=Planete("a","oui",100,10,50,100,200)
planete2=Planete("b","non",200,20,350,200,900)
planete1Predite=PlanetePredite("a","oui",100,10,50,100,200,"gazeuse")

print("Type de planete :",planete1Predite.getTypePlanete())

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 1, 6, 4, 5])
o = OutilsAnalyse()
print(o.coefCorrel(x, y))
kmeans=o.kMeans(2,l)
for grp in kmeans:
    print(grp.getPoints())