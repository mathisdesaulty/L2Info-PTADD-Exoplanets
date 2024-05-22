from Point import Point

class Planete: #définition de la classe Planete et initialisation de toutes ses variables
    nom=""
    masse=0
    rayon=0
    rayonOrbite=0
    periodeOrbite=0

    def __init__(self,nom,masse,rayon,rayonOrbite,periodeOrbite): #définition du constructeur de la classe Planete
        self.nom=nom
        self.masse=masse
        self.rayon=rayon
        self.rayonOrbite=rayonOrbite
        self.periodeOrbite=periodeOrbite
    
    def getNom(self): #fonctions qui renvoient les valeurs contenues dans les variables respectives
        return self.nom
    
    def getMasse(self):
        return self.masse
    
    def getRayon(self):
        return self.rayon
    
    def getRayonOrbite(self):
        return self.rayonOrbite
    
    def getPeriodeOrbite(self):
        return self.periodeOrbite
    
    def convertirPlaneteEnPoint(self):
        return Point(self.nom,[self.masse,self.rayon,self.rayonOrbite,self.periodeOrbite])

    def afficher(self):
        print("Nom :",self.nom)
        print("Masse :",self.masse)
        print("Rayon :",self.rayon)
        print("Rayon d'orbite :",self.rayonOrbite)
        print("Période d'orbite :",self.periodeOrbite)

class PlanetePredite(Planete): #définition de la classe PlanetePredite qui hérite de la classe Planete
    typePlanete=""

    def __init__(self,nom,masse,rayon,rayonOrbite,periodeOrbite,typePlanete): #définition du constructeur de la classe PlanetePredite qui appelle le constructeur de la classe Planete
        super().__init__(nom,masse,rayon,rayonOrbite,periodeOrbite)
        self.typePlanete=typePlanete

    def getType(self): #renvoie le type de la planète prédite
        return self.typePlanete
    
    def setType(self,typePlanete): #modifie le type de la planète prédite
        self.typePlanete=typePlanete

    def convertirPlanetePrediteEnPoint(self):
        return Point(self.nom,[self.masse,self.rayon,self.rayonOrbite,self.periodeOrbite],self.typePlanete)
    
    def afficher(self):
        super().afficher()
        print("Type de planète :",self.typePlanete)