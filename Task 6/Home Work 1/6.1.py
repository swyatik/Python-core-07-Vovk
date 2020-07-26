"""Заповнити один список випадковими числами,
інший - введеними з клавіатури числами,
в третій записати суми відповідних елементів перших двох.
Вивести вміст списків на екран.
"""
from random import randint

# check whether the entered number is correct
def check():
    while True:
        try:
            num = int(input('Input your number from -99 to 99: '))
            if -100 < num < 100:
                return num
            else:
                print('    ERROR: your number must be from -99 to 99')
                continue
        except:
            print('    ERROR: your number must be an integer')


n = 10  # amount of numbers in list
randomList = []
userList = []
sumList = []

for i in range(n):
    userList.append(check())

print(f'__{"_"*4*n}')
print('%12s' %'randomList: ', end='')
for i in range(n):
    randomList.append(randint(15, 20))
    print('%3d' % randomList[i], end='')

for i in range(n):
    sumList.append(randomList[i] + userList[i])

print()
print('%12s' %'userList: ', end='')
for i in userList:
    print('%3d' %i, end='')

print()
print('%12s' %'sumList: ', end='')
for i in sumList:
    print('%3d' %i, end='')

print()