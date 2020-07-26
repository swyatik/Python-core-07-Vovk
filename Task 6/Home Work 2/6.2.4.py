"""Знайти максимальний елемент серед мінімальних елементів стовпців матриці.
"""

from random import randint

#  function of prints a matrix
def printMatrix(matrix):
    for x in matrix:
        for z in x:
            print("%4d " % z, end="")
        print()


column = 5
row = 4

matrix = [[] for i in range(row)]
for i in matrix:
    for j in range(column):
        i.append(randint(1, 20))

printMatrix(matrix)
matrix2 = [[] for i in range(column)]
for i in range(column):
    for j in range(row):
        matrix2[i].append(matrix[j][i])

max = 0
for i in matrix2:
    minNumber = min(i)
    if minNumber > max: max = minNumber

print(f'The maximum element among \nthe minimum elements of the matrix columns: {max}')