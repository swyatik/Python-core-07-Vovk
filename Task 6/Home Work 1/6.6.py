"""У другому списку зберегти індекси парних елементів першого списку.
Наприклад, якщо дано список зі значеннями 8, 3, 15, 6, 4, 2,
то  другий треба заповнити значеннями 1, 4, 5, 6
(або 0, 3, 4, 5 - якщо індексація починається з нуля),
оскільки саме в цих позиціях першого масиву стоять парні числа.
"""
from random import randint

randList = []
withoutNegative = []
print('Our list:')
for i in range(20):
    randList.append(randint(-20, 20))
    print('%2d' %randList[i], end='  ')
print()

print('List of indices of even numbers:')
indexEven = [i for i in range(len(randList)) if randList[i] % 2 == 0]
for i in indexEven:
    print('%2d' %i, end='  ')
print()