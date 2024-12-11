from cythonMethod import cythonMethod
from time import time
from csvSaver import saveResults

def cythonSimulation(xvals, nRepeats):
    results = []
    for n in xvals:
        times = []
        for m in range(nRepeats):
            startTime = time()
            total_points = cythonMethod(n)
            elapsed_time = time() - startTime
            estimated_pi = float(total_points) / n * 4  # Estimer π
            times.append(elapsed_time)
        results.append(sum(times)/nRepeats)
    return results

if __name__ == "__main__":
    xvals = [10**m for m in range(1, 5)]  # Nombre de points par itération
    nRepeats = 1
    results = cythonSimulation(xvals, nRepeats)
    print(list(results))
    saveResults("Cython", xvals, results)