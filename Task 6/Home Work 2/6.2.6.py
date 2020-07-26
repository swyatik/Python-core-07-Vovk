'''У матриці 10x10 поміняти значення елементів у кожному рядку,
розташовані відповідно на головній та бічній діагоналях.
'''
from random import randint

#  function of prints a matrix
def printMatrix(matrix):
    for i in matrix:
        for j in i:
            print("%4d " % j, end="")
        print()


rowColumn = 10
matrix = [[] for i in range(rowColumn)]

for i in matrix:
    for j in range(rowColumn):
        i.append(randint(1, 20))

print('\nMatrix to replace elements:')
print(f'{"_" * 5 * rowColumn}')
printMatrix(matrix)

for i in range(rowColumn):
        temp = matrix[i][i]
        matrix[i][i] = matrix[rowColumn - 1 - i][i]
        matrix[rowColumn - 1 - i][i] = temp

print('\nMatrix after element replacement:')
print(f'{"_" * 5 * rowColumn}')
printMatrix(matrix)
