from OutilsAnalyse import OutilsAnalyse
import numpy as np
from Point import Point
from GroupeDePoints import GroupeDePoints
import csv

o = OutilsAnalyse.getInstance()

with open('DatasetModif.csv',newline='') as f:
    tableau=[]
    lire=csv.reader(f)
    for ligne in lire:
        tableau.append(ligne)

planete1=Point("Planète 1",[float(tableau[5][1]),float(tableau[5][2]),float(tableau[5][3])])
planete2=Point("Planète 2",[float(tableau[25][1]),float(tableau[25][2]),float(tableau[25][3])])
planete3=Point("Planète 2",[float(tableau[2000][1]),float(tableau[2000][2]),float(tableau[2000][3])])
planetesAPredire=GroupeDePoints("Groupe de points",[planete1,planete2,planete3])
    
del tableau[0]

grpDePoints=GroupeDePoints("Groupe de planètes")

for ligne in tableau:
    planete=Point(ligne[0],[float(ligne[1]),float(ligne[2]),float(ligne[3])],ligne[4])
    grpDePoints.ajoutePoint(planete)

planetesEntrainees=o.entrainerKNN(2,grpDePoints)

print(o.predictionPoint(planete1,planetesEntrainees).getTypePlanete())
o.predictionGroupe(planetesAPredire,planetesEntrainees).afficher()