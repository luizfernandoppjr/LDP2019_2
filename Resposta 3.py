#Problema 3
import numpy as np
import time
from IPython.display import clear_output

pista = 100
c = []
p = []

cavalos = int(input())

for i in range(cavalos):
    r = input().split()
    r = [float(j) for j in r]
    c.append(r)

p = [0]*len(c)

while max(p) < pista:
    clear_output()
    for i in range(cavalos):
        p[i] += int(abs(np.random.normal(c[i][0], c[i][1])))
        print("{:.0f} {}{}{}".format(i+1, '-'*p[i], ' '*(pista-p[i]), '|'))
    time.sleep(0.5)

print("Cavalo {:.0f} Venceu!".format(p.index(max(p))+1))
