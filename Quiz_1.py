'''
Questao 1: (2 pontos)
Dado um parâmetro n, a funcão deve retornar True se n é primo e False caso contrário
Ex:
    11 -> True
    15 -> False
'''

import math

def prime(n):
    primos = set(range(2, n + 1))
    for i in range(2, math.ceil(n ** (1 / 2))):
        if i in primos:
            primos -= set(range(i, n + 1, i)[1:])
    return primos


'''
Questao 2: (2 pontos)
A entrada é uma lista de inteiros e a saida deves ser a lista sem números repetidos
Ex:
    [1,2,3,1,5,2] -> [1,2,3,5]
    [15,15,15,15] -> [15]
'''

def unicos(L):
    conj = set(L)
    return list(conj)


'''
Questao 3: (3 pontos)
Seja d(n) definido como a soma dos divisores inteiros de n. Se d(a) = b e d(b) = a,
sendo a ≠ b, então a e b são um "par amigável" de números.
A funcao tem como entrada uma tupla com 2 inteiros
e saida True ou False se estes números sao um par amigável"
Ex:
    (220, 284) -> True   #Obs: d(220) = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 286, o mesmo para d(284)
    (500, 30) -> False
'''

def amigavel(ab):
    def d(n):
        som = 0
        for i in range(1, n+1):
            if (n % i) == 0:
                som += i
        return som
    if d(ab[0]) == d(ab[1]):
        return True
    else:
        return False


'''
Questao 4: (3 pontos)
Dada uma lista L, retorne ela ordenada. Nao usar o sort interno do python!
Ex:
    [5,8,1,2,0,3,4] - > [0, 1, 2, 3, 4, 5, 8]
    [5,4,3,2,1] -> [1, 2, 3, 4, 5]
'''

def sort(L):
    menor = []
    lista_pivo = []
    maior = []

    if len(L) <= 1:
        return L
    else:
        pivo = L[0]
        for i in L:
            if i < pivo:
                menor.append(i)
            elif i > pivo:
                maior.append(i)
            else:
                lista_pivo.append(i)
        menor = sort(menor)
        maior = sort(maior)
        return menor + lista_pivo + maior



print(prime(17))
print(unicos([1,2,2,3,4,5,5,5,5]))
print(amigavel((220,284)))
print(sort([1,6,3,6,8,3,2,0,1]))