import numpy as np
import pandas as pd
import sklearn as sk
from sklearn.cluster import KMeans

from GroupeDePoints import GroupeDePoints

class OutilsAnalyse:
    
    def __init__(self):
        print("")

    def convertirPointsEnListe(self,grp): #Fonction qui convertit un GroupeDePoint en Liste pour l'utiliser dans d'autres fonctions
        grpDePoints=[]
        for point in grp:
            grpDePoints.append([point.getX(),point.getY()])
        return grpDePoints
        
    def coefCorrel(self, grp1, grp2):
        return np.corrcoef(grp1, grp2)[0, 1]
    
    def kNN():
        return
        
    def NP():
        return
    
    def kMeans(self,nbClusters,grp):
        grpDePoints=self.convertirPointsEnListe(grp)
        kmeans=KMeans(n_clusters=nbClusters,random_state=0,n_init="auto").fit(grpDePoints).labels_
        resultat=[]
        for i in range(nbClusters):
            resultat.append(GroupeDePoints(str(i),[]))
        print("a",resultat[0].getNom())
        for i in range(len(kmeans)):
            for j in range(nbClusters):
                if resultat[j].getNom()==str(kmeans[i]):
                    resultat[j].ajoutePoint(grp[i])
        return resultat

    
    def prediction():
        return
    
    def predirePlanete():
        return