"""У змінній записаний текст. Словом вважається послідовність непорожніх символів,
    які йдуть підряд, слова розділені одним або більше пробілом.
    Програмно створіть словник, в якому ключами є слова з речення,
    а значеннями – кількість входження в речення.
"""

def replacePunct(string, punct):
    """Функція приймає 2 аргументи: string- рядок(текст),
        punct- список розділових знаків. Замінює розділові знаки на пробіли
        і повертає список слів з тексту у нижньому регістрі"""
    listReplace = string
    for pun in punct:
        listReplace = listReplace.replace(pun, ' ')
    return [item.lower() for item in listReplace.split()]

def main():
    # запитуємо текст в користувача
    while True:
        text = input('Enter the text:\n')
        if text == '': print('    Sorry, but your text cannot be empty!')
        else: break

    # tuple з розділовими знаками можна доповнити будь-якими
    punctuation = ('.', ',', chr(33), '?', ':', ';', '-', '"', '(', ')')
    # створюємо пустий словник
    dictText = {}
    # створюємо список слів тексту без розділових знаків
    listText = replacePunct(text, punctuation)
    # пробігаємось по списку і якщо слова немає в словнику,
    # то додаємо його та підраховуємо кількість входжень
    for item in listText:
        if item not in dictText:
            dictText[item] = listText.count(item)

    # виводимо словник в алфавітному порядку на екран
    for item in sorted(dictText):
        print(f'{item:15s} : {dictText[item]:<2d}')


if __name__ == "__main__":
    main()