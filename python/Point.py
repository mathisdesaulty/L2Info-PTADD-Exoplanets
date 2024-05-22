class Point: #définition de la classe Point et initialisation de toutes ses variables
    nom=""
    coord=[]
    typePlanete=""

    def __init__(self,nom,coordonnees,typePlanete=""): #définition du constructeur de la classe Point
        self.nom=nom
        self.coord=coordonnees
        self.typePlanete = typePlanete

    def getNom(self):
        return self.nom

    def getCoord(self): #retourne les coordonnées du point
        return self.coord
    
    def getTypePlanete(self):
        return self.typePlanete
    
    def setTypePlanete(self, typePlanete):
        self.typePlanete = typePlanete
    
    def copiePoint(self):
        return Point(self.nom, self.coord, self.typePlanete)
    
    def toString(self):
        return f"Nom: {self.nom}, Type de planète: {self.typePlanete}, Coordonnées: {self.coord}"