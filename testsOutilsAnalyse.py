from OutilsAnalyse import OutilsAnalyse
import numpy as np
from Point import Point
from GroupeDePoints import GroupeDePoints

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

grp1 = GroupeDePoints("grp1", [point1, point2, point3, point4, point5, point6])
point = Point("test1", [2, 1])

print(o.kNN(4, point, grp1))
print(o.convertirPointsEnTypePlanete(grp1))


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
