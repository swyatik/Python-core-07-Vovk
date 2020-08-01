"""Задано символьний рядок.
    Розробити програму, яка вилучає з цього рядка всі повторні
    входження цифр і знаків арифметичних операцій.
"""
def delRepeat(string, arithmeticList):
    temp = ''
    for symbol in string:
        if symbol.isdigit() or symbol in arithmeticList:
            if symbol in temp: pass
            else: temp += symbol
        else: temp += symbol

    return temp


def main():
    while True:
        myArithmetic = ['+', '-', '*', '/', '=']
        userString = input("Enter your line: ")
        if userString == '': print('    Error: the line must not be empty! try again. ')
        else: break
    print(delRepeat(userString, myArithmetic))

if __name__ == "__main__":
    main()