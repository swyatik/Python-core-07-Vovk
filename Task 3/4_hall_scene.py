'''Чи можна в квадратному залі площею S помістити круглу сцену радіусом R так,
щоб від стіни до сцени був прохід не менше K?'''
from math import sqrt

s = int(input('Input your area of square (S): '))
r = int(input('Input your radius of scene (R): '))
k = int(input('Input your width of passage (K): '))
k2 = sqrt(s) / 2 - r
if k2 >= k:
    print("    Yes, the scene can be set.")
else:
    print("    Sorry, but the scene can't be set.")

