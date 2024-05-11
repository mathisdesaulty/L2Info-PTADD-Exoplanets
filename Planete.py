class Planete: #définition de la classe Planete et initialisation de toutes ses variables
    nom=""
    brillance=0
    masse=0
    rayon=0
    rayonOrbite=0
    periodeOrbite=0
    excentricite=0

    def __init__(self,nom,brillance,masse,rayon,rayonOrbite,periodeOrbite,excentricite): #définition du constructeur de la classe Planete
        self.nom=nom
        self.brillance=brillance
        self.masse=masse
        self.rayon=rayon
        self.rayonOrbite=rayonOrbite
        self.periodeOrbite=periodeOrbite
        self.excentricite=excentricite
    
    def getNom(self): #fonctions qui renvoient les valeurs contenues dans les variables respectives
        return self.nom
    
    def getBrillance(self):
        return self.brillance
    
    def getMasse(self):
        return self.masse
    
    def getRayon(self):
        return self.rayon
    
    def getRayonOrbite(self):
        return self.rayonOrbite
    
    def getPeriodeOrbite(self):
        return self.periodeOrbite
    
    def getExcentricite(self):
        return self.excentricite

    def afficher(self):
        print("Nom :",self.nom)
        print("Brillance :",self.brillance)
        print("Masse :",self.masse)
        print("Rayon :",self.rayon)
        print("Rayon d'orbite :",self.rayonOrbite)
        print("Période d'orbite :",self.periodeOrbite)
        print("Excentricité :",self.excentricite)

class PlanetePredite(Planete): #définition de la classe PlanetePredite qui hérite de la classe Planete
    type=""

    def __init__(self,nom,brillance,masse,rayon,rayonOrbite,periodeOrbite,excentricite,typePlanete): #définition du constructeur de la classe PlanetePredite qui appelle le constructeur de la classe Planete
        super().__init__(nom,brillance,masse,rayon,rayonOrbite,periodeOrbite,excentricite)
        self.typePlanete=typePlanete

    def getType(self): #renvoie le type de la planète prédite
        return self.type
    
    def setType(self,type): #modifie le type de la planète prédite
        self.type=type
    
    def afficher(self):
        print("Nom :",self.nom)
        print("Brillance :",self.brillance)
        print("Masse :",self.masse)
        print("Rayon :",self.rayon)
        print("Rayon d'orbite :",self.rayonOrbite)
        print("Période d'orbite :",self.periodeOrbite)
        print("Excentricité :",self.excentricite)
        print("Type de planète :",self.type)