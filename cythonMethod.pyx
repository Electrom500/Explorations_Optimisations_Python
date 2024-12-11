from libc.math cimport sqrt  # Pour utiliser sqrt en C
from random import random
from time import time

# Déclaration des types pour améliorer les performances
cpdef int cythonMethod(int n):
    cdef int validPoints = 0  # Compte les points à l'intérieur du cercle
    cdef double x, y
    
    for _ in range(n):
        x = random()
        y = random()
        if sqrt(x * x + y * y) <= 1:
            validPoints += 1
    return validPoints