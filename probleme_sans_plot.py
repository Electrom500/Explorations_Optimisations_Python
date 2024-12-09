from random import random
import numpy as np
from math import cos, sin, pi
from time import time

# Initialisation des variables
valeurs = []
temps_execution = []  # Liste pour stocker les temps d'exécution
xvals = [10**m for m in range(1, 7)]  # Nombre de points par itération
points = []

# Calcul des points dans le cercle pour chaque itération
for i, n in enumerate(xvals):
    debut = time()
    points = np.array([p for _ in range(n) if np.linalg.norm(p := np.array([random(), random()]) - 0.5) <= 0.5])
    fin = time() - debut
    valeurs.append(len(points) / n)
    temps_execution.append(fin)


# Estimation finale de π
valeurs = np.array(valeurs) * 4

print(valeurs)
print(temps_execution)
