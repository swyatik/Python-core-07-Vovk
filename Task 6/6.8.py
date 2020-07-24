"""У списку випадкових цілих чисел поміняти місцями
мінімальний і максимальний елементи.
"""

from random import randint

randList = []
for i in range(10):
    randList.append(randint(1, 25))

print(randList)
minNumber = min(randList)
minIndex = randList.index(minNumber)
maxIndex = randList.index(max(randList))
randList[minIndex] = max(randList)
randList[maxIndex] = minNumber
print(randList)
print('min: %2d' %minNumber)
print('max: %2d' %randList[minIndex])

