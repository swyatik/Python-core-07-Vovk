'''Написати функцію arithmetic, яка приймає 3 аргументи:
перші 2 - числа, третій - операцію, яка повинна бути здійснена над ними.
 Якщо третій аргумент +, додати їх; якщо -, то відняти; * - помножити;
 / - розділити (перше на друге).
 В інших випадках повернути рядок "Невідома операція".
 '''


def arithmetic(num1, num2, sign):
    '''Виконує прості арифметичні дії над числами.
    Приймає три аргументи: 1-ий та 2-ий числа(int or float),
    3-ій - знак арифметичної дії "+, -, *, /"
    Повертає результат.'''
    operations = ('+', '-', '*', '/')
    return eval(num1 + sign + num2) if sign in operations else 'Невідома операція'


def askCheck(name):
    '''Запитує в користувача числа та перевіряє їх на відповідність умові(int or float).
    Приймає один аргумент: рядок із запитом до користувача
    повертає рядок з числом або виводить повідомлення про помилку до моменту
    введення користувачем відповідного значення.'''
    while True:
        number = input(f'{name}')
        if '.' in number and number.count('.') == 1:
            if ''.join(number.split('.')).isdigit():
                return number
        else:
            try:
                n = int(number)
                return number
            except:
                print('    Error: Your number must be an integer or float')


def main():
    number1 = askCheck('Enter first number: ')
    number2 = askCheck('Enter second number: ')
    sign = input('Enter arithmetic sign: ')
    try:
        print(f'{number1} {sign} {number2} = {arithmetic(number1, number2, sign)}')
    except ZeroDivisionError:
        print('    Sorry, but you cannot divide by zero! Try else')

if __name__ == "__main__":
    main()
