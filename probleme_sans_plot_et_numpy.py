from random import random
from math import cos, sin, pi, sqrt
from time import time

# Initialisation des variables
valeurs = []
temps_execution = []  # Liste pour stocker les temps d'exécution
xvals = [10**m for m in range(1, 7)]  # Nombre de points par itération


# Calcul des points dans le cercle pour chaque itération
for n in xvals:
    debut = time()
    points = [
        (x, y)
        for _ in range(n)
        if (x := random()) and (y := random()) and sqrt((x - 0.5) ** 2 + (y - 0.5) ** 2) <= 0.5
    ]
    fin = time() - debut
    
    valeurs.append(len(points) / n)
    temps_execution.append(fin)


# Estimation finale de π
valeurs = [v * 4 for v in valeurs]

print(valeurs)
print(temps_execution)
