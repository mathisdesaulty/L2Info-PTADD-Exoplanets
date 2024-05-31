import csv
with open("DatasetModif.csv",newline='') as f:
    tab=[]
    lire=csv.reader(f)
    for ligne in lire:
        tab.append(ligne)
print(tab[0],tab[1])
print(len(tab))
with open("DatasetNew.csv",'w',newline='') as f:
    ecrire=csv.writer(f)
    for ligne in tab:
        if ligne[4]=="Gas Giant":
            ecrire.writerow(["Geante gazeuse"])
        elif ligne[4]=="Neptune-like":
            ecrire.writerow(["Geante de glace"])
        elif ligne[4]=="Super Earth":
            ecrire.writerow(["Super Terre"])
        elif ligne[4]=="Terrestrial":
            ecrire.writerow(["Terrestre"])
        else:
            ecrire.writerow("")