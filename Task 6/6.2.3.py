"""Матриця 5x4 заповнюється введенням з клавіатури (крім останніх елементів рядків).
Програма повинна обчислювати суму введених елементів кожного рядка і
записувати її в останній рядок. Наприкінці слід вивести отриману матрицю.
"""
#  function of prints a matrix
def printMatrix(matrix):
    for i in matrix:
        for j in i:
            print("%4d " % j, end="")
        print()


# enter and check if the entered number is correct
def check():
    while True:
        try:
            num = int(input(f'Enter the integer number: '))
            return num
        except:
            print('    ERROR: your number must be an integer')


matrix = [[] for i in range(4)]
for i in matrix:
    sumRow = 0
    for j in range(4):
        i.append(check())
        sumRow += i[j]
    i.append(sumRow)

print('Your matrix:')
printMatrix(matrix)