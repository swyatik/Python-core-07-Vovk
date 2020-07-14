'''Відома грошова сума.
Розміняти її купюрами 200, 100, 10 і монетою 1 грн.,
якщо це можливо.'''

allMoney = int(input('Input your amount of money: '))
money = allMoney
if money >= 200:
    twoHundred = money // 200
    print(twoHundred, ' pieces for 200 hrn.')
    money %= 200
if money >= 100:
    oneHundred = money // 100
    print(oneHundred, ' pieces for 100 hrn.')
    money %= 100
if money >= 10:
    ten = money // 10
    print(ten, ' pieces for 10 hrn.')
    money %= 10
if money >= 1:
    one = money
    print(one, ' pieces for 1 hrn.')
