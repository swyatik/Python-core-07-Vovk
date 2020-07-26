'''Дві матриці заповнюються введенням з клавіатури.
В елементи третьої матриці такої ж розмірності записати
більші з відповідних елементів перших двох.
'''

#  function of prints a matrix
def printMatrix(matrix):
    for i in matrix:
        for j in i:
            print("%4d " % j, end="")
        print()

# enter and check if the entered number is correct
def check(name):
    while True:
        try:
            num = int(input(f'{name}: '))
            return num
        except:
            print('    ERROR: your number must be an integer')

column = check('Enter the number of column items')
row = check('Enter the number of line items')
matrixOne = [[] for i in range(row)]
matrixTwo = [[] for i in range(row)]
matrixThree = [[] for i in range(row)]

print('    Enter the element of the first matrix:')
for i in range(row):
    for j in range(column):
        matrixOne[i].append(check(f'matrixOne {i}-{j}'))

print('    Enter the element of the second matrix:')
for i in range(row):
    for j in range(column):
        matrixTwo[i].append(check(f'matrixTwo {i}-{j}'))

for i in range(row):
    for j in range(column):
        if matrixOne[i][j] >= matrixTwo[i][j]:
            matrixThree[i].append(matrixOne[i][j])
        else:
            matrixThree[i].append(matrixTwo[i][j])

print(f'{"_" * 5 * column}')
printMatrix(matrixOne)
print(f'{"_" * 5 * column}')
printMatrix(matrixTwo)
print(f'{"_" * 5 * column}')
printMatrix(matrixThree)
