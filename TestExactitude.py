from sklearn.model_selection import LeaveOneOut
from sklearn.metrics import accuracy_score
from OutilsAnalyse import OutilsAnalyse
from Point import Point
from GroupeDePoints import GroupeDePoints
import csv


o = OutilsAnalyse.getInstance()

with open('DatasetModif.csv',newline='') as f:
    tableau=[]
    lire=csv.reader(f)
    for ligne in lire:
        tableau.append(ligne)
   
del tableau[0]

grpDePoints=GroupeDePoints("Groupe de planètes")

for ligne in tableau:
    planete=Point(ligne[0],[float(ligne[1]),float(ligne[2]),float(ligne[3])],ligne[4])
    grpDePoints.ajoutePoint(planete)






loo = LeaveOneOut()
vraiesValeurs = []
predictions = []
for trainIndex, testIndex in loo.split(grpDePoints.getPoints()):
    # Séparer les données d'entraînement et de test
    pointsEntraines = []
    for i in trainIndex:
        pointsEntraines.append(grpDePoints.getPoints()[i])
    pointExclus = grpDePoints.getPoints()[testIndex[0]]
     
    knn = o.entrainerKNN(2, GroupeDePoints(pointExclus))
    
    # Faire une prédiction sur le point exclus
    prediction = o.predictionType(pointExclus, knn)
    
    # Ajouter la vraie valeur et la prédiction aux listes
    vraiesValeurs.append(pointExclus.getTypePlanete())
    predictions.append(prediction)

# Calculer le score d'exactitude
accuracy = accuracy_score(vraiesValeurs, predictions)
print("Score d'exactitude :", accuracy)