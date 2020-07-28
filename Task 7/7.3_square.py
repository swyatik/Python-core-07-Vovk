'''. Написати функцію square, яка приймає 1 аргумент - сторону квадрата,
і повертає 3 значення (за допомогою кортежу):
периметр квадрата, площу квадрата і діагональ квадрата.
'''

def square(side):
    return (side * 4, side ** 2, side * 2 ** 0.5)

def askCheck():
    '''Запитує в користувача сторону квадрату та перевіряє
    чи в рядку міститься числове значення(int or float).
    Не приймає аргументів та повертає число або виводить
    повідомлення про помилку до моменту введення користувачем
     відповідного значення..'''
    while True:
        number = input('Enter the length of the side of the square: ')
        if '.' in number and number.count('.') == 1:
            if ''.join(number.split('.')).isdigit():
                return abs(float(number))
        else:
            try:
                n = abs(int(number))
                return n
            except:
                print('    Error: Your number must be an integer or float')

def main():
    side = square(askCheck())
    p, s, d = side
    print(side)
    print(f"{'The perimeter of the square: ':38s}{p:.2f}")
    print(f"{'The area of the square: ':38s}{s:.2f}")
    print(f"The length of diagonal of the square: {d:.2f}")

if __name__ == "__main__":
    main()