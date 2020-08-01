"""Задано символьний рядок.
    Розробити програму, яка будує і друкує
    в алфавітному порядку множину малих,
    множину великих латинських  літер, які містяться
    у заданому рядку, і множину цифр, яких немає у рядку.
"""

def printSet(userSet):
    usrSetSort = sorted(userSet)
    for i in range(len(usrSetSort)):
        if i == 0: print('{', end='')
        if i < len(usrSetSort) - 1: print(f'{usrSetSort[i]}, ', end='')
        else: print(f'{usrSetSort[i]}}}')

def main():
    while True:
        userString = set(input('Enter your line: '))
        if userString == '':
            print('    Error: the line must not be empty! try again. ')
        else:
            break
    numberSet = set([i for i in range(10)])
    leterLower = set([chr(i) for i in range(97, 123)])
    leterUpper = set([chr(i) for i in range(65, 91)])

    print('A set of lowercase letters:')
    printSet(userString.intersection(leterLower))
    print('A set of uppercase letters:')
    printSet(userString.intersection(leterUpper))
    print('A set of digits that are not in the string:')
    printSet(numberSet.difference(set([int(number) for number in userString if number.isdigit()])))


if __name__ == "__main__":
    main()