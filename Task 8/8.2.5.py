"""Задано два символьних рядка із малих і великих латинських літер та цифр.
    Розробити програму, яка будує і друкує в алфавітному порядку множину літер,
    які є в обох масивах, і множини літер окремо першого і другого масивів.
"""
def printSetSort(userSet):
    usrSetSort = sorted(userSet)
    for i in range(len(usrSetSort)):
        if i == 0: print('{', end='')
        if i < len(usrSetSort) - 1: print(f'{usrSetSort[i]}, ', end='')
        else: print(f'{usrSetSort[i]}}}')


def main():
    while True:
        userString1 = input("String 1: ")
        if userString1 == '':
            print('    Error: the line must not be empty! try again. ')
        else:
            while True:
                userString2 = input("String 2: ")
                if userString2 == '':
                    print('    Error: the line must not be empty! try again. ')
                else:
                    break
            userString1 = set([leter for leter in userString1 if leter.isalpha()])
            userString2 = set([leter for leter in userString2 if leter.isalpha()])
            break
    intersect = userString2.intersection(userString1)
    print(f'{" "*5}The set of letters that are in both arrays:')
    printSetSort(intersect)
    print(f'{" "*5}The set of letters of the first arrays:')
    printSetSort(userString1)
    print(f'{" "*5}The set of letters of the second arrays:')
    printSetSort(userString2)


if __name__ == "__main__":
    main()