import sys

def calculer_moyenne(valeurs):
    if len(valeurs) == 0:
        return 0
    return sum(valeurs) / len(valeurs)

def addition(valeurs):
    s = 0
    for i in range(len(valeurs)) :
        s+=valeurs[i]
    return s

if __name__ == "__main__":
    # Lire les arguments de ligne de commande (en ignorant le premier qui est le nom du script)
    valeurs = list(map(float, sys.argv[1:]))
    moyenne = addition(valeurs)
    print(moyenne)
