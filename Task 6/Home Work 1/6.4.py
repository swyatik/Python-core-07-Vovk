"""Випадкові числа в діапазоні від -5 до 5 розкласти на два списки:
в один помістити тільки додатні, у другий - тільки від’ємні.
Числа, рівні нулю, ігнорувати. Вивести на екран всі згенеровані
випадкові числа і елементи обох списків.
"""
from random import randint

randList = []
positiveList = []
negativeList = []
print('Elements of our list:')
for i in range(20):
    randList.append(randint(-5, 5))
    if randList[i] > 0: positiveList.append(randList[i])
    elif randList[i] < 0: negativeList.append(randList[i])
    else: pass
    print('%2d' %randList[i], end='  ')

print()
print('Positive numbers of our list:')
for i in positiveList:
    print('%2d' %i, end='  ')

print()
print('Negative numbers of our list:')
for i in negativeList:
    print('%2d' %i, end='  ')

