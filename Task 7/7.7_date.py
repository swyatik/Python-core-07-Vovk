"""Написати функцію date, яка приймає 3 аргументи - день, місяць і рік.
Повернути True, якщо така дата є в нашому календарі, і False - в іншому випадку.
"""
from datetime import date as d

def date(day, month, year):
    """функція, яка приймає 3 аргументи - день, місяць і рік.
    Повертає True, якщо така дата є в нашому календарі, і False - в іншому випадку."""
    try:
        d(year, month, day)
        return True
    except:
        return False

def askCheck(name):
    while True:
        string = input(f'Enter the {name}: ')
        if string.isdigit():
            return abs(int(string))
        else:
            print("    Error: your number must be an integer!")

def main():
    day = askCheck('day')
    month = askCheck('month')
    year = askCheck('year')
    if date(day, month, year):
        print(f'    Ok, {day}.{month}.{year} exist in the calendar!')
    else:
        print(f'    Sorry, but {day}/{month}/{year} does not exist in the calendar!')

if __name__ == "__main__":
    main()



