'''Залежно від вибору користувача, обчислити площу або прямокутника,
або трикутника, або круга. Якщо обрані прямокутник або трикутник,
то треба запросити довжини сторін; круга – його радіус.'''
from math import sqrt
from math import pi

area = None
choice = int(input('Input your number (1-rectangle, 2-triangle, 3-circle): '))
if choice == 1:
    length = int(input('Input length of a rectangle: '))
    width = int(input('Input width of a rectangle: '))
    area = length * width
elif choice == 2:
    side1 = int(input('Input side1 of a triangle: '))
    side2 = int(input('Input side2 of a triangle: '))
    side3 = int(input('Input side3 of a triangle: '))
    p = (side1 + side2 + side3) / 2
    area = sqrt(p * (p - side1) * (p - side2) * (p - side3))
elif choice == 3:
    radius = int(input('Input radius of a circle: '))
    area = radius**2 * pi
else:
    print('Sorry, but you have not selected any shapes!')

if choice == 1 or choice == 2 or choice == 3:
    print('Area = {}'.format(area))