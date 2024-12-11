from random import random
from math import cos, sin, pi, sqrt
from time import time
from numba import jit, prange
from numpy import zeros

def run_probleme():
    # Initialisation des variables
    valeurs = []
    temps_execution = []  # Liste pour stocker les temps d'exécution
    xvals = [10**m for m in range(1, 7)]  # Nombre de points par itération


    # Calcul des points dans le cercle pour chaque itération
    for n in xvals:
        debut = time()
        points = compute_points3(n)
        fin = time() - debut
        
        valeurs.append(len(points) / n)
        temps_execution.append(fin)


    # Estimation finale de π
    valeurs = [v * 4 for v in valeurs]

    print(valeurs)
    print(temps_execution)

@jit
def compute_points(n):
    points = []
    for _ in range(n):
        x = random()
        y = random()
        if sqrt((x - 0.5) ** 2 + (y - 0.5) ** 2) <= 0.5:
            points.append((x, y))
    return points

@jit(nopython=True, parallel=True)
def compute_points2(n):
    points = zeros((n, 2))
    count = 0
    for i in range(n):
        x = random()
        y = random()
        if sqrt((x - 0.5) ** 2 + (y - 0.5) ** 2) <= 0.5:
            points[count, 0] = x
            points[count, 1] = y
            count += 1
    return points[:count]

@jit(nopython=True, parallel=True)
def compute_points3(n):
    points = zeros((n, 2))
    count = 0
    for i in prange(n):  # prange au lieu de range
        x = random()
        y = random()
        if sqrt((x - 0.5) ** 2 + (y - 0.5) ** 2) <= 0.5:
            points[count, 0] = x
            points[count, 1] = y
            count += 1
    return points[:count]

run_probleme()
