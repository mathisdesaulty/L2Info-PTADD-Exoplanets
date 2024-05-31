from OutilsAnalyse import OutilsAnalyse
from Point import Point
from GroupeDePoints import GroupeDePoints
import csv
import sys


if __name__ == "__main__":
    o = OutilsAnalyse.getInstance()

    with open('pythonFinal/DatasetModifFinal.csv',newline='') as f:
        tableau=[]
        lire=csv.reader(f)
        for ligne in lire:
            tableau.append(ligne)
            
    valeurs = list(map(float, sys.argv[1:]))

    planete1=Point("Planète 1",[float(valeurs[0]),float(valeurs[1]),float(valeurs[2])])
        
    del tableau[0]

    grpDePoints=GroupeDePoints("Groupe de planètes")

    for ligne in tableau:
        planete=Point(ligne[0],[float(ligne[1]),float(ligne[2]),float(ligne[3])],ligne[4])
        grpDePoints.ajoutePoint(planete)

    planetesEntrainees=o.entrainerKNN(2,grpDePoints)

    print(o.predictionType(planete1,planetesEntrainees))