#1. Supondo que o diretório atual esteja vazio, crie os meios (Python) para tornar possível o seguinte código.
#In [ ]:
import os; os.rename("dir1/dir2/dir3/file.txt", "dir1/dir4/dir5/file.txt")
#2. Faça um programa, que dado um n informado pelo usuário, retorne o seguinte array $nxn$:
# n impar
array([[1, 0, 3, 0, 5, ..., n],
       [0, 2, 0, 4, 0, ..., 0],
       [0, 0, 3, 0, 5, ..., n],
       [0, 0, 0, 4, 0, ..., 0],
       [0, 0, 0, 0, 5, ..., n],
                ...          ,
       [0, 0, 0, 0, 0, ..., n]])
#3. Simule uma corrida de cavalos.
#O primeiro input contém um int positivo n, que representa o número de cavalos.
#Os seguintes n inputs são 2 floats, velocidade média do cavalo e a variação.
#Simule uma corrida de cavalos em que cada turno a distância que cada cavalo percorrer é um número aleatório de sua distribuição normal.
#Cada turno dura 0.5 segundos. A pista possui 100 unidades de distância.

Ex:

3
1.0 0.1
1.1 0.11
1.1 0.2

final:

"""
1 -----------------------------------------------------------------------------------------           |
2 ----------------------------------------------------------------------------------------------------|
3 --------------------------------------------------------------------------------------------------- |
Cavalo 2 venceu!
"""