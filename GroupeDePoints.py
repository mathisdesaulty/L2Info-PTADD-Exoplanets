from Point import Point

class GroupeDePoints: #définition de la classe GroupeDePoints et initialisation de toutes ses variables
    nom=""
    points=[]

    def __init__(self,nom,points): #définition du constructeur de la classe GroupeDePoints
        self.nom=nom
        self.points=points
    
    def getPoints(self):
        return self.points
    
    def getCentre(self): #retourne le centre de tous les points contenus dans le groupe de points
        totalX=0
        totalY=0
        for point in self.points: #parcours tous les points contenus dans la variable de classe "points"
            totalX+=point.getX() #les points sont ajoutés dans les variables de total respectives
            totalY+=point.getY()
        return [totalX/len(self.points),totalY/len(self.points)] #renvoie la moyenne des X et des Y du groupe de points
            
    def getNbPoints(self): #retourne le nombre de points contenus dans le groupe de points
        return len(self.points)