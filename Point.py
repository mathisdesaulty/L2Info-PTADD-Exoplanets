class Point: #définition de la classe Point et initialisation de toutes ses variables
    nom=""
    coord=[]

    def __init__(self,nom,coordonnees): #définition du constructeur de la classe Point
        self.nom=nom
        self.coord=coordonnees

    def getNom(self):
        return self.nom

    def getCoord(self): #retourne les coordonnées du point
        return self.coord
    
    def toString(self):
        return self.nom+""+str(self.coord)