# -*- coding: utf-8 -*-

from java.util.concurrent import Executors, Callable
from random import random
from math import sqrt
from time import time

# Tâche Callable pour la sous-tâche Monte Carlo
class MonteCarloTask(Callable):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def call(self):
        points = 0
        for _ in range(self.start, self.end):
            x = random()
            y = random()
            if sqrt((x - 0.5) ** 2 + (y - 0.5) ** 2) <= 0.5:
                points += 1
        return points

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
    
    executor.shutdown()  # Arrêter l'exécuteur de manière gracieuse
    return total_points

# Boucle principale pour exécuter la simulation Monte Carlo pour différentes valeurs de n
xvals = [10**m for m in range(1, 7)]  # Nombre de points par itération
values = []
times = []

for n in xvals:
    startTime = time()
    total_points = jythonMethod(n, num_threads=4)  # Utiliser 4 threads
    times.append(time() - startTime)
    estimated_pi = float(total_points) / n * 4  # Estimer π
    values.append(estimated_pi)

# Afficher les résultats
# print(values)
print(times)