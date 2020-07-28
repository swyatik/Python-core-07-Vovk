"""Написати функцію is_year_leap, приймає 1 аргумент - рік,
і повертає True, якщо рік високосний, і False в іншому випадку.
"""


def askCheck():
    '''Запитує в користувача рік та перевіряє його на відповідність умові(int).
    Приймає один аргумент: рядок із запитом до користувача
    повертає рядок з числом або виводить повідомлення про помилку до моменту
    введення користувачем відповідного значення.'''
    while True:
        number = input('Input your year: ')
        try:
            return abs(int(number))
        except:
            print('    Error: Your number must be an integer')

def is_year_leap(year):
    '''is_year_leap, приймає 1 аргумент - рік,
    і повертає True, якщо рік високосний, і False в іншому випадку.'''
    return True if year % 4 == 0 else False

def main():
    year = askCheck()
    if is_year_leap(year): print(f"    {year} is a leap year")
    else: print(f"    {year} is not a leap year")

if __name__ == "__main__":
    main()
