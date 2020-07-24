"""Згенерувати 20 випадкових цілих чисел в діапазоні від -5 до 4,
записати їх в список. Порахувати кількість додатних,
від’ємних і нульових елементів.
Вивести на екран елементи списку і пораховані кількості.
"""

from random import randint

randList = []
for i in range(20):
    randList.append(randint(-5, 4))

positiveNumber = 0
negativeNumber = 0
zero = 0
print('Elements of our list:')
for i in randList:
    if i > 0: positiveNumber += 1
    elif i < 0: negativeNumber += 1
    else: zero += 1
    print('%2d' %i, end='  ')

print()
print("The number of positive numbers in the list: %2d" %positiveNumber)
print("The number of negative numbers in the list: %2d" %negativeNumber)
print("Zero values in the list: %2d" %zero)