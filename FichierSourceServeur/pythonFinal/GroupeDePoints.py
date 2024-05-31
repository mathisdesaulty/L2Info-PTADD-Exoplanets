from Point import Point

class GroupeDePoints: #définition de la classe GroupeDePoints et initialisation de toutes ses variables
    nom=""
    points=[]

    def __init__(self,nom,points=[]): #définition du constructeur de la classe GroupeDePoints
        self.nom=nom
        self.points=points

    def getNom(self):
        return self.nom
    
    def getPoint(self,nb): #retourne le point à l'indice donné
        return self.points[nb]
    
    def getPoints(self):
        return self.points
    
    def getCentre(self): #retourne le centre de tous les points contenus dans le groupe de points
        total=[0 for i in range(len(self.points[0].getCoord()))]
        for point in self.points: #parcours de tous les points contenus dans la variable de classe "points"
            for i in range(len(point.getCoord())):
                total[i]=total[i]+point.getCoord()[i] #ajoute chaque coordonnées de chaque point à leur total respectif
        for i in range(len(total)): #parcours le total
            total[i]=total[i]/len(self.points) #divise chaque nombre total par le nombre de points
        return total
            
    def getNbPoints(self): #retourne le nombre de points contenus dans le groupe de points
        return len(self.points)
    
    def ajoutePoint(self,point): #ajoute un point au groupe de points
        self.points.append(point)
    
    def afficher(self): #fonction d'affichage
        print(self.nom+":") #affiche le nom du groupe de point + ":" et saute une ligne à la fin du print
        for point in self.points:
            print(point.toString()) #affiche les points un par un en utiliant la fonction toString de la classe Point