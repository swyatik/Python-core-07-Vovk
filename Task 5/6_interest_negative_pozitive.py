'''Для чисел, що вводяться користувачем,
визначити відсоток додатних та від’ємних чисел.
При введенні числа 0 закінчити роботу.
'''

amountNumbers = 0
negative = 0
pozitive = 0

def check():
    while True:
        try:
            num = int(input('Input your number: '))
            return num
        except:
            print('    ERROR: your number must be an integer')

while True:
    number = check()
    amountNumbers += 1
    if number == 0:
        print(f'{"*" * 15}')
        print('Pozitive: %5.1f%%' % round(pozitive * 100 / amountNumbers, 2))
        print('Negative: %5.1f%%' % round(negative * 100 / amountNumbers, 2))
        break
    elif number > 0:
        pozitive += 1
    else:
        negative += 1