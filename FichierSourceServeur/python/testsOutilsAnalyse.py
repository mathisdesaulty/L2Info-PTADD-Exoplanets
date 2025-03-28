import sys
from OutilsAnalyse import OutilsAnalyse
import numpy as np
from Point import Point
from GroupeDePoints import GroupeDePoints
import csv
from Planete import Planete
from Planete import PlanetePredite

if __name__ == "__main__":

    o = OutilsAnalyse.getInstance()
    o.kMeans

    grpPlanetes=[]

    with open('python/DatasetModif.csv',newline='') as f:
        tableau=[]
        lire=csv.reader(f)
        for ligne in lire:
            tableau.append(ligne)

    # Lire les arguments de ligne de commande (en ignorant le premier qui est le nom du script)
    valeurs = list(map(float, sys.argv[1:]))

    ptPlanete1=Point("Point 1",valeurs)
    # ptPlanete2=Point("Point 2",[float(tableau[25][1]),float(tableau[25][2]),float(tableau[25][3]),float(tableau[25][4])])
    # planetesAPredire=GroupeDePoints("Groupe de points",[ptPlanete1,ptPlanete2])
        
    del tableau[0]

    for ligne in tableau:
        planete=PlanetePredite(ligne[0],float(ligne[1]),float(ligne[2]),float(ligne[3]),float(ligne[4]),ligne[5])
        grpPlanetes.append(planete)

    grpDePoints=GroupeDePoints("Groupe de planètes")

    for planete in grpPlanetes:
        grpDePoints.ajoutePoint(planete.convertirPlanetePrediteEnPoint())

    planetesEntrainees=o.entrainerKNN(2,grpDePoints)

    print(o.predictionPoint(ptPlanete1,planetesEntrainees))