"""Змінити послідовність стовпців матриці так,
щоб елементи її першого рядка були відсортовані за зростанням.
"""
from random import randint

#  function of prints a matrix
def printMatrix(matrix):
    for item in matrix:
        for jtem in item:
            print("%4d " % j, end="")
        print()

column = 10
row = 5

matrix = [[] for i in range(row)]

for item in matrix:
    for j in range(column):
        item.append(randint(1, 20))

print('\nMatrix to sorting elements:')
print(f'{"_" * 5 * column}')
printMatrix(matrix)

# відсортований кортеж (елемент, його індекс)
sortRowIndex = sorted([(matrix[0][i], i) for i in range(column)])
# замінюємо елементи матриці на основі кортежу(sortRowIndex)
for i in range(row):
    for j in range(int(column/2) if column % 2 == 0 else int(column/2) + 1):
        temp = matrix[i][j]
        matrix[i][j] = matrix[i][sortRowIndex[j][1]]
        matrix[i][sortRowIndex[j][1]] = temp

print('\nMatrix after sorting elements:')
print(f'{"_" * 5 * column}')
printMatrix(matrix)

