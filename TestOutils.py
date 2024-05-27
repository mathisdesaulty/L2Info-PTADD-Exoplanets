import numpy as np
import pandas
import sklearn

from Point import Point
from GroupeDePoints import GroupeDePoints
from OutilsAnalyse import OutilsAnalyse

p1=Point("a",[-1,1,5])
p2=Point("b",[3,5,-1])
p3=Point("c",[0,2,6])
p4=Point("d",[4,4,0])
p5=Point("e",[2,7,-2])
p6=Point("f",[-2,-1,8])
l=[p1,p2,p3,p4,p5,p6]
grp=GroupeDePoints("grp",l)

print("Coordonnées :",p1.getCoord())
print("Nombre de points dans le groupe :",grp.getNbPoints())
print("Centre :",grp.getCentre())
print("Type de planete :",p1.getTypePlanete())

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 1, 6, 4, 5])
o = OutilsAnalyse()
print(o.coefCorrel(x, y))

kmeans=o.kMeans(2,grp)
for grp in kmeans:
    grp.afficher()