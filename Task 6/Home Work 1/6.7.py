"""У списку знайти елементи, які в ньому зустрічаються тільки один раз,
 і вивести їх на екран.
"""
from random import randint

randList = []
print('Our list:')
for i in range(20):
    randList.append(randint(0, 10))
    print('%2d' %randList[i], end='  ')
print()

once = [i for i in randList if randList.count(i) == 1]
print('List of numbers that are once:')
for i in once:
    print('%2d' %i, end='  ')
print()