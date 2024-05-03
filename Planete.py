class Planete: #définition de la classe Planete et initialisation de toutes ses variables
    nom=""
    brillance=""
    masse=0
    rayon=0
    rayonOrbite=0
    periodeOrbite=0
    excentricite=0

    def _init_(self,nom,brillance,masse,rayon,rayonOrbite,periodeOrbite,excentricite): #constructeur de la classe Planete
        self.nom=nom
        self.brillance=brillance
        self.masse=masse
        self.rayon=rayon
        self.rayonOrbite=rayonOrbite
        self.periodeOrbite=periodeOrbite
        self.excentricite=excentricite

class PlanetePredite(Planete): #définition de la classe PlanetePredite qui hérite de la classe Planete
    typePlanete=""

    def _init_(self,typePlanete):
        self.typePlanete=typePlanete