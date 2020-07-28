'''. Написати функцію season, яка приймає 1 аргумент - номер місяця (від 1 до 12),
і повертає пору року, якій цей місяць належить (зима, весна, літо або осінь).
'''

def season(number):
    """функція season, приймає 1 аргумент - номер місяця (від 1 до 12),
    і повертає пору року, якій цей місяць належить (зима, весна, літо або осінь).
    """
    if number < 3 or number == 12: return 'winter'
    if number < 6: return 'spring'
    if number < 9: return 'summer'
    if number < 12: return 'autumn'

def askCheck():
    '''Запитує в користувача місяць та перевіряє його на відповідність умові(int).
    Приймає один аргумент: рядок із запитом до користувача
    повертає рядок з числом або виводить повідомлення про помилку до моменту
    введення користувачем відповідного значення..'''
    while True:
        number = input('Input your month: ')
        if number.isdigit() and 13 > int(number) > 0: return int(number)
        else: print('    Error: Your number must be an integer')

def main():
    month = askCheck()
    print(f'{month} is a month of {season(month)}')

if __name__ == "__main__":
    main()
