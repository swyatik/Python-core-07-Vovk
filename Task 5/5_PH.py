'''Дано число P  і число H.
Користувач вводить послідовність чисел.
Визначити: суму тих чисел, які менше P; добуток чисел,
які більші за H; кількість чисел, що знаходяться
в діапазоні значень від P до H. При введенні числа рівного P або H,
припинити обчислення та вивести результат.
'''
p = None
h = None
sumLessP = None
productGreaterH = None
amountPH = 0


def check(name='sequence number', numberP=None):
    while True:
        try:
            num = int(input(f"Input your number {name}: "))
            if name == 'p':
                return num
            elif name == 'h':
                if num > numberP:
                    return num
                else:
                    print(f'    Error: Your number must be >{numberP}')
                    continue
            else:
                return num
        except:
            print('    Error: Your number must be an integer')


while True:
    if p == None:
        p = check('p')
    if h == None:
        h = check('h', p)
    number = check()
    if number == p or number == h:
        print(f"{'*' * 35}")
        if sumLessP == None:
            print(f'There are no numbers <{p}.')
        else:
            print(f'The sum of numbers <{p}: {sumLessP} ')
        if productGreaterH == None:
            print(f'There are no numbers >{h}.')
        else:
            print(f'The product of numbers >{h}: {productGreaterH}')
        if amountPH == 0:
            print(f'There are no numbers >{p} and <{h}.')
        else:
            print(f'The amount of numbers >{p} and <{h}: {amountPH}')
        break
    else:
        if number < p:
            sumLessP = sumLessP + number if sumLessP != None else number
        elif number > h:
            productGreaterH = productGreaterH * number if productGreaterH != None else number
        else:
            amountPH += 1
