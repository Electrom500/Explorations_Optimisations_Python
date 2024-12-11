from random import random
from math import sqrt
from time import time
from csvSaver import saveResults

def pythonMethod(n):
    validPoints = 0 # Compte les points à l'intérieur du cercle
    for _ in range(n):
        x = random()
        y = random()
        if sqrt(x * x + y * y <= 1):
            validPoints += 1
    return validPoints

def pythonSimulation(xvals, nRepeats):
    results = []
    for n in xvals:
        times = []
        for m in range(nRepeats):
            startTime = time()
            total_points = pythonMethod(n)
            elapsed_time = time() - startTime
            estimated_pi = float(total_points) / n * 4  # Estimer π
            times.append(elapsed_time)
        results.append(sum(times)/nRepeats)
    return results

# Appeler la fonction principale
if __name__ == "__main__":
    xvals = [10**m for m in range(1, 7)]  # Nombre de points par itération
    nRepeats = 100
    results = pythonSimulation(xvals, nRepeats)
    print(results)
    saveResults("Python", xvals, results)