import timeit

input_sizes = [10**i for i in range(2, 4)]

python_times = []
cython_times = []

# Measure execution times for each input size
for n in input_sizes:
    python_time = timeit.timeit(
        f"pythonOnlyMethod.computePi({n})",
        setup="import pythonOnlyMethod",
        number=100,
        globals=globals()
    )
    cython_time = timeit.timeit(
        f"cythonMethod.computePi({n})",
        setup="import cythonMethod",
        number=100,
        globals=globals()
    )
    
    # Store results
    python_times.append(python_time)
    cython_times.append(cython_time)

    # Print results for current n
    print(f"n={n}: Python={python_time:.6f}s, Cython={cython_time:.6f}s, "
          f"Speedup={python_time / cython_time:.2f}x")

print(f"Python : {python_times}")
print(f"Cython : {cython_times}")