from OutilsAnalyse import OutilsAnalyse
import numpy as np
from Point import Point
from GroupeDePoints import GroupeDePoints
import csv
from Planete import Planete
from Planete import PlanetePredite

#Test OutilsAnalyse.coefCorrel
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 1, 6, 4, 5])
o = OutilsAnalyse.getInstance()
print(o.coefCorrel(x, y))




#Test OutilsAnalyse.kNN
point1 = Point("pt1", [2, 0], "gazeuse")
point2 = Point("pt2", [1, 2], "gazeuse")
point3 = Point("pt3", [2, 2],"gazeuse")
point4 = Point("pt4", [1, -1],"terrestre")
point5 = Point("pt5", [4, -2],"terrestre")
point6 = Point("pt6", [-1, 2],"terrestre")

point11 = Point("pt11", [1, 0])
point22 = Point("pt22", [1, 1])
point33 = Point("pt33", [-3, -3])


grp1 = GroupeDePoints("grp1", [point1, point2, point3, point4, point5, point6])
grp2 = GroupeDePoints("grp1", [point11, point22, point33])
point = Point("test1", [2, 1])

print(o.kNN(2, point, grp1))
#o.predictionKNN(2,grp1,grp2).afficher()



pt1 = Point("pt1", [2, 0, 0])
pt2 = Point("pt2", [10, 10, 5])
pt3 = Point("pt3", [2, 2, 1])
pt4 = Point("pt4", [14, 8, 4])
pt5 = Point("pt5", [1, 2, 2])
pt6 = Point("pt6", [12, 7, 9])

grp2 = GroupeDePoints("grp2", [pt1, pt2, pt3, pt4, pt5, pt6])

"""kmeans=o.kMeans(2,grp2)
for groupe in kmeans:
    groupe.afficher()
"""

grpPlanetes=[]

with open('DatasetModif.csv',newline='') as f:
    tableau=[]
    lire=csv.reader(f)
    for ligne in lire:
        tableau.append(ligne)

ptPlanete1=Point("Point 1",[float(tableau[5][1]),float(tableau[5][2]),float(tableau[5][3]),float(tableau[5][4])])
ptPlanete2=Point("Point 2",[float(tableau[25][1]),float(tableau[25][2]),float(tableau[25][3]),float(tableau[25][4])])
grpDePlanetes=GroupeDePoints("Groupe de points",[ptPlanete1,ptPlanete2])
    
del tableau[0]

for ligne in tableau:
    planete=Planete(ligne[0],float(ligne[1]),float(ligne[2]),float(ligne[3]),ligne[4])
    grpPlanetes.append(planete)

grpDePoints=GroupeDePoints("Groupe de planètes")

for planete in grpPlanetes:
    grpDePoints.ajoutePoint(planete.convertirPlaneteEnPoint())

print(grpDePoints.getNbPoints())
grpDePlanetes.afficher()

o.predictionKNN(2,grpDePoints,grpDePlanetes).afficher()