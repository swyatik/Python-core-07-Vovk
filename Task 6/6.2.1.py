"""Порахувати суми кожного рядка і кожного стовпця матриці.
Доповнити її стовпцем, який містить суми елементів рядків та рядком,
елементами якого є суми елементів стовпців.
"""
from random import randint

# check whether the entered number is correct
def check(name):
    while True:
        try:
            num = int(input(f'Input the number of {name} (>=2): '))
            if num >= 2:
                return num
            else:
                print('    ERROR: your number must be greater than 2 or 2')
                continue
        except:
            print('    ERROR: your number must be an integer')

#  prints a matrix
def printMatrix(name, matrix, column):
    print(f'{"_" * 5 * column}\n{name} list:')
    for i in matrix:
        for j in i:
            print("%4d " % j, end="")
        print()

row = check('rows')  # row
column = check('columns')  # columns

numbers = [[] for i in range(row)]  # create empty matrix
print(f'{"_"*5*column}\nOur list:')
# add element to matrix and print it elements
for i in numbers:
    for j in range(column):
        i.append(randint(1, 10))
        print("%4d " % i[j], end="")
    print()

# create a new row for the sum in the columns
numbers.append([])
for i in range(column):
    sumColumn = 0
    for j in range(row):
        sumColumn += numbers[j][i]
    numbers[row].append(sumColumn)

# add new column for the sum in the row
for i in numbers:
    i.append(sum(i))

printMatrix('New', numbers, column)
