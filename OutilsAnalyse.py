import numpy as np
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

from Point import Point
from GroupeDePoints import GroupeDePoints
from sklearn.cluster import KMeans

class OutilsAnalyse:
    
    _instance = None  #Instance unique du singleton
    
    def __init__(self):
        if OutilsAnalyse._instance is not None:
            raise Exception("Cette classe est un singleton, utilisez la méthode getInstance() pour obtenir l'instance.")
    
    @staticmethod
    def getInstance(): #Methode d'appel et de création d'OutilsAnalyse
        if OutilsAnalyse._instance is None:
            OutilsAnalyse._instance = OutilsAnalyse()
        return OutilsAnalyse._instance
    
        
    def convertirPointsEnListe(self,grp): #Fonction qui convertit un GroupeDePoints en Liste pour l'utiliser dans d'autres fonctions
        grpDePoints=[]
        for point in grp.getPoints():
            grpDePoints.append(point.getCoord())
        return grpDePoints
    
    def convertirPointsEnTypePlanete(self, grp): #Fonction qui convertit un GroupeDePoints en Liste de typePlanete
        grpDePoints=[]
        for point in grp.getPoints():
            grpDePoints.append(point.getTypePlanete())
        return grpDePoints
        
    def coefCorrel(self, grp1, grp2):
        #A modifier car doit prendre en compte les parametres d'un groupe de points
        return np.corrcoef(grp1, grp2)[0, 1]
    
    
    #nbVoisin : int, point : Point, grp : groupeDePoints 
    def kNN(self, nbVoisin, point, grp):
        grpDePoints=self.convertirPointsEnListe(grp) #Prend tous les points contenus dans le groupe de points
        typeDePoints=self.convertirPointsEnTypePlanete(grp)#Prend le typePlanete de tous les points contenus dans le groupe de points
        LabelEncoder().fit_transform(typeDePoints)#Encode les typePlanete pour qu'ils soient utilisables par kNN
        pointCoordonnees = [point.getCoord()] #Prend les coordonnees du point qu'on cherche
        knn = KNeighborsClassifier(n_neighbors=nbVoisin, metric='minkowski',algorithm='ball_tree') #Création de l'algo kNN avec paramètres
        knn.fit(grpDePoints, typeDePoints) #Entraineement de l'algo Knn sur les coordonnées d'un groupe de point et leur typePlanete
        return knn.predict(pointCoordonnees) #Prediction du point recherché avec le groupe de point entrainé, retourne un String etant le typePlanete prédit
        
    
    def kMeans(self,nbCluster,grp): #Algorithme des KMeans qui prend un nombre de cluster et un groupe de points en paramètre et qui renvoie plusieurs groupes de points (clusters)
        grpDePoints=self.convertirPointsEnListe(grp)
        kmeans=KMeans(n_clusters=nbCluster,random_state=0,n_init="auto").fit(grpDePoints).labels_ #effectue l'algorithme des KMeans
        resultat=[]
        for i in range(nbCluster): #création des clusters à renvoyer
            resultat.append(GroupeDePoints(str(i),[]))
        for i in range(len(kmeans)): #ajoute chaque point au cluster auquel il appartient selon l'algorithme des KMeans
            for j in range(nbCluster):
                if resultat[j].getNom()==str(kmeans[i]):
                    resultat[j].ajoutePoint(grp.getPoint(i))
        return resultat
    
    #nbVoisin : int, grpApprentissage : groupeDePoints, grpPrediction : groupeDePoints
    def predictionKNN(self, nbVoisin, grpApprentissage, grpPrediction):
        resultat = GroupeDePoints("Groupe de point prediction Knn",) #Créer un groupe de point vide
        for i in range(0, grpPrediction.getNbPoints()): #Parcours la lsite des points qu'on veut prédire
            copieDuPoint = grpPrediction.getPoints()[i].copiePoint() #Copie ces points pour ne pas écraser ceux fournies si jamais on veut les traiter
            copieDuPoint.setTypePlanete(self.kNN(nbVoisin,copieDuPoint, grpApprentissage)) #Modification du typePlanete de la copie grace à la méthode kNN
            resultat.ajoutePoint(copieDuPoint)
        return resultat #Le résultat est un groupe de point, ce sont les mêmes points que ceux fournies dans grpPrediction excepté leur typePlanete
        
        
        
    
    def prediction():
        return
    
    def predirePlanete():
        return