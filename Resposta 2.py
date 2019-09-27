#Problema 2
import numpy as np


n = int(input())
m = np.zeros([n,n], dtype=int)
for i in range(n):
    for j in range(i, n, 2):
        m[i,j] = j+1


print(m)

