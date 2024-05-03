class Point: #définition de la classe Point et initialisation de toutes ses variables
    nom=""
    x=0
    y=0

    def __init__(self,nom,x,y): #définition du constructeur de la classe Point
        self.nom=nom
        self.x=x
        self.y=y

    def getX(self): #retourne la coordonnée X du point
        return self.x
    
    def getY(self): #retourne la coordonnée Y du point
        return self.y