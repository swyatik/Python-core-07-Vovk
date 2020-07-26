"""Заповнити список випадковими додатними і від’ємними цілими числами.
Вивести його на екран. Видалити з списку всі від’ємні елементи і знову вивести.
"""
from random import randint

randList = []
withoutNegative = []
print('Our list:')
for i in range(20):
    randList.append(randint(-5, 5))
    print('%2d' %randList[i], end='  ')

print()
randList = [i for i in randList if i >= 0]
print('New list without negative numbers:')
for i in randList:
    print('%2d' %i, end='  ')
print()
