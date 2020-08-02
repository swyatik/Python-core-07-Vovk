"""Задано символьний рядок,.
    Розробити програму, яка знаходить групи цифр, записаних підряд,
    і вилучає із них всі початкові нулі, крім останнього,
    якщо за ним знаходиться крапка. Друкує модифікований масив по сорок символів у рядку.
"""
def printArray(string, n):
    '''Функція друкує текст зі заданою кількістю символів в рядку.
        Приймає 2 аргументи, string-рядок(текст), та n-кількість символів'''
    newArray = list(string)
    lengthStr = len(string)
    if lengthStr > n:
        count = n
        for i in range(len(string)//n):
            newArray.insert(count, '\n')
            count += n + 1
        print(''.join(newArray))
    else:
        print(string)


def main():
    userStr = ''
    while True:
        userStr = input('Enter your text:\n')
        if userStr == '':
            print('    Error: the line must not be empty! try again. ')
        else: break

    while userStr.find('00.') != -1:
        userStr = userStr.replace('00.', '0.')

    printArray(userStr, 40)


if __name__ == "__main__":
    main()