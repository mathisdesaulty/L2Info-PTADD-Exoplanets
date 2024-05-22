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
    
tableauModif=[]
for liste in tableau:
    if liste[0]=="" or liste[1]=="" or liste[2]=="" or liste[3]=="" or liste[4]=="":
        print(liste)
    else:
        tableauModif.append(liste)
"""
with open("DatasetModif.csv",'w',newline="") as f:
    ecrire=csv.writer(f)
    for i in tableauModif:
        ecrire.writerow(i)
"""
