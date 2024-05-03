class Point: #définition de la classe Point et initialisation de toutes ses variables
    nom=""
    x=0
    y=0

    def _init_(self,nom,x,y): #définition du constructeur de la classe Point
        self.nom=nom
        self.x=x
        self.y=y

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y