from libc.math cimport sqrt  # Pour utiliser sqrt en C
from random import random

# Déclaration des types pour améliorer les performances
def computePi(int n) -> float:
    cdef int i, inside_circle = 0  # Compte les points à l'intérieur du cercle
    cdef double x, y, distance
    
    # Génération des points
    for i in range(n):
        x = random()
        y = random()
        distance = sqrt((x - 0.5) ** 2 + (y - 0.5) ** 2)
        if distance <= 0.5:
            inside_circle += 1
    
    return (inside_circle / n) * 4.0  # Estimation de pi
