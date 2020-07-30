"""Створити список, що містить цифри, літери алфавіту (великі та малі), спеціальні символи;
    Розділити список на декілька, кожний з яких містить тільки цифри, тільки літери тощо;
    Конвертувати списки в кортежі;
    Ввести з клавіатури почергово цифру, літеру чи спецсимвол і повернути відповідно індекс входження у відповідний кортеж;
    Відобразити реверс одного з кортежів.
"""
def main():
    userList = [i for i in range(1, 10)] + [chr(i) for i in range(32, 48)]\
               + [chr(i) for i in range(65, 123)]

    numberList = []
    charList = []
    symbolList = []
    for item in userList:
        if item in [i for i in (range(1, 10))]: numberList.append(item)
        elif item.isalpha(): charList.append(item)
        else: symbolList.append(item)

    numberTuple = tuple(numberList)
    charTuple = tuple(charList)
    symbolTuple = tuple(symbolList)

    print(f'My list: \n{userList}')
    print(f'List of numbers: \n{numberList}')
    print(f'List of chars: \n{charList}')
    print(f'List of symbols: \n{symbolList}')
    print(f'Tuple of numbers: \n{numberTuple}')
    print(f'Tuple of chars: \n{charTuple}')
    print(f'Tuple of symbols: \n{symbolTuple}')
    while True:
        userSymbol = input("Input your symbol, letter, number or '00' for exit: ")
        if userSymbol == '00':
            break
        elif not userSymbol.isdigit() and userSymbol not in userList:
            print(f'{" "*4}"{userSymbol}" is not in tuples')
        elif userSymbol.isdigit():
            if int(userSymbol) in numberTuple:
                print(f'{" "*4}Index "{userSymbol}" in numberTuple is {numberTuple.index(int(userSymbol))}')
            else:
                print(f'{" " * 4}"{userSymbol}" is not in tuples')
        elif userSymbol.isalpha():
            print(f'{" "*4}Index "{userSymbol}" in charTuple is {charTuple.index(userSymbol)}')
        else:
            print(f'{" "*4}Index "{userSymbol}" in symbolTuple is {symbolTuple.index(userSymbol)}')

    print(f'Revers numberTuple: \n{numberTuple[::-1]}')

if __name__ == "__main__":
    main()