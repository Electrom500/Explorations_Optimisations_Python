import time

n = 10000000 #10M
a = 0

moy = 0

m=10
for j in range(m):
    start = time.time()
    for k in range(n):
        a = k
    end = time.time()
    moy = moy + (end-start)/m
print("temps moyen d'execution = ", moy)
