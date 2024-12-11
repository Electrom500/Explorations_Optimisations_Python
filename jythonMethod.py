# -*- coding: utf-8 -*-

from java.util.concurrent import Executors, Callable
from random import random
from math import sqrt
from time import time
from csvSaver import saveResults

# Tâche Callable pour la sous-tâche Monte Carlo
class MonteCarloTask(Callable):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def call(self):
        validPoints = 0 # Compte les points à l'intérieur du cercle
        for _ in range(self.start, self.end):
            x = random()
            y = random()
            if sqrt(x * x + y * y <= 1):
                validPoints += 1
        return validPoints

# Fonction pour effectuer la tâche complète de Monte Carlo en utilisant la parallélisation
def jythonMethod(n, num_threads):
    # Créer un pool de threads fixe en utilisant le service Executor de Java
    executor = Executors.newFixedThreadPool(num_threads)
    futures = []
    
    # Diviser le travail en num_threads parties
    chunk_size = n // num_threads
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else n
        task = MonteCarloTask(start, end)  # Définir la tâche avec la plage
        futures.append(executor.submit(task))  # Soumettre la tâche à l'exécuteur
    
    # Collecter les résultats de tous les threads
    total_points = 0
    for future in futures:
        total_points += future.get()  # Bloquer et obtenir le résultat de chaque thread
    
    executor.shutdown()  # Arrêter l'exécuteur
    return total_points

# Fonction pour exécuter la simulation pour différents nombres de points
def jythonSimulation(xvals, nRepeats, nThreads):
    results = []
    for n in xvals:
        times = []
        for m in range(nRepeats):
            startTime = time()
            total_points = jythonMethod(n, nThreads)  # Utiliser les threads
            elapsed_time = time() - startTime
            estimated_pi = float(total_points) / n * 4  # Estimer π
            times.append(elapsed_time)
        results.append(sum(times)/nRepeats)
    return results

# Appeler la fonction principale
if __name__ == "__main__":
    xvals = [10**m for m in range(1, 7)]  # Nombre de points par itération
    nRepeats = 100
    nThreads = 4  # Nombre de threads à utiliser
    results = jythonSimulation(xvals, nRepeats, nThreads)
    print(results)
    saveResults("Jython", xvals, results)