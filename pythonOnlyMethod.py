from random import random
from math import sqrt

def computePi(n):
    inside_circle = 0  # Compte les points à l'intérieur du cercle
    
    # Génération des points
    for i in range(n):
        x = random()
        y = random()
        distance = sqrt((x - 0.5) ** 2 + (y - 0.5) ** 2)
        if distance <= 0.5:
            inside_circle += 1
    
    return (inside_circle / n) * 4.0  # Estimation de pi