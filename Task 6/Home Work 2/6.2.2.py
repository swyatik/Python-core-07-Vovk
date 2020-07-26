"""Сформувати матрицю з чисел від 0 до 999, вивести її на екран.
   Порахувати кількість двозначних чисел в ній.
"""
#  function of prints a matrix
def printMatrix(matrix):
    for i in matrix:
        for j in i:
            print("%4d " % j, end="")
        print()

# determine the optimal number of rows and columns
param = (0, 0, 1000)
for i in range(1, int(1000**0.5)):
    if 1000 % i == 0:
        if 1000/i - i < param[2]:
            param = (i, int(1000/i), int(1000/i) - i)

matrix = [[] for i in range(param[1])]
n = 0
amount = 0
for i in range(param[1]):
   for j in range(n, n + param[0]):
       matrix[i].append(j)
       if len(str(n)) == 2: amount += 1
       n += 1

printMatrix(matrix)
print(f'There are {amount}- two-digit numbers in the matrix.')
