import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from Point import Point
from GroupeDePoints import GroupeDePoints

class OutilsAnalyse:
    
    def __init__(self):
        print("")
        
    def convertirPointsEnListe(self,grp): #Fonction qui convertit un groupeDePoints en Liste pour l'utiliser dans d'autres fonctions
        grpDePoints=[]
        for point in grp:
            grpDePoints.append([point.getX(),point.getY()])
        return grpDePoints
    
        
    def coefCorrel(self, grp1, grp2):
        #A modifier car doit prendre en compte les parametres d'un groupe de points
        return np.corrcoef(grp1, grp2)[0, 1]
    
    
    #nbVoisin : int, point : Point, grp : groupeDePoints 
    def kNN(self, nbVoisin, point, grp):
        pointCoordonnees = [[point.getX(), point.getY()]] #Prend les coordonnees du point qu'on cherche
        grpDePoints = grp.getPoints()  #Prend tous les points contenus dans le groupe de points
        grpCoordonnees=self.convertirPointsEnListe(grpDePoints) #Prend les coordonnees de tous ces points
        nbrs = NearestNeighbors(nbVoisin, metric='minkowski',algorithm='ball_tree').fit(grpCoordonnees) #Algo KNN
        indices = nbrs.kneighbors(pointCoordonnees)[1][0] #On prend l'index auxquels sont stockes les plus proches voisins de pointCoordonees dans la variable groupeDePoints
        resultat = []
        for i in indices:
            resultat.append(grpDePoints[i]) #On prend les points qui sont les plus proches voisins dans groupeDePoint grace aux index obtenus plus tot
        return resultat #On retourne une liste de points
        
    def NP():
        return

    
    def Kmean():
        return
    
    def prediction():
        return
    
    def predirePlanete():
        return
    
    
    
