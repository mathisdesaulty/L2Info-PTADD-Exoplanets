class GroupeDePoints: #définition de la classe GroupeDePoints et initialisation de toutes ses variables
    nom=""
    points=[]

    def _init_(self,nom,points): #définition du constructeur de la classe GroupeDePoints
        self.nom=nom
        self.points=points
    
    def getCentre(self): #retourne le centre de tous les points contenus dans le groupe de points
        0#pas fini

    def getNbPoints(self): #retourne le nombre de points contenus dans le groupe de points
        return len(self.points)