from OutilsAnalyse import OutilsAnalyse
import numpy as np
from Point import Point
from GroupeDePoints import GroupeDePoints

#Test OutilsAnalyse.coefCorrel
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 1, 6, 4, 5])
o = OutilsAnalyse()
print(o.coefCorrel(x, y))




#Test OutilsAnalyse.kNN
point1 = Point("test1", 2, 0)
point2 = Point("test1", 1, 2)
point3 = Point("test1", 2, 2)
point4 = Point("test1", 1, -1)
point5 = Point("test1", 4, -2)
point6 = Point("test1", -1, 2)

grp1 = GroupeDePoints("grp1", [point1, point2,point3, point4, point5, point6])
point = Point("test1", 2, 1)


print(o.kNN(4, point, grp1))
