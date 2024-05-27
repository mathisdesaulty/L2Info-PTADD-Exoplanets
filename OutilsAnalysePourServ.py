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
        
    #Entraine un algo kNN avec un groupe
    #nbVoisin : int, grpApprentissage : groupeDePoints,
    def entrainerKNN(self, nbVoisin, grp):
        grpDePoints=self.convertirPointsEnListe(grp) #Prend tous les points contenus dans le groupe de points
        typeDePoints=self.convertirPointsEnTypePlanete(grp)#Prend le typePlanete de tous les points contenus dans le groupe de points
        LabelEncoder().fit_transform(typeDePoints)#Encode les typePlanete pour qu'ils soient utilisables par kNN
        knn = KNeighborsClassifier(n_neighbors=nbVoisin, metric='minkowski',algorithm='ball_tree')
        return knn.fit(grpDePoints, typeDePoints) #Retourne une fonction entrainée sur les données passé dans la variable grp
        
    #Predit les points individuellement
    #point : Point, knn : grpEntraine obtenu avec entrainerKNN
    def predictionType(self, point, knn):
        pointCoordonnees = [point.getCoord()] #Prend les coordonnees du point qu'on cherche
        return knn.predict(pointCoordonnees)[0] #Prediction du point recherché avec le groupe de point entrainé, retourne un String etant le typePlanete prédit