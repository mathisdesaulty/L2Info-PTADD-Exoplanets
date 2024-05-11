from OutilsAnalyse import OutilsAnalyse
import numpy as np
from Point import Point
from GroupeDePoints import GroupeDePoints
from Planete import Planete
import csv

grpPlanetes=[]

with open('DatasetModif.csv',newline='') as f:
    tableau=[]
    lire=csv.reader(f)
    for ligne in lire:
        tableau.append(ligne)
    
for liste in tableau:
    planete=Planete(liste[0],liste[1],liste[2],liste[3],liste[4],liste[5],liste[6])
    grpPlanetes.append(planete)

planete.afficher()