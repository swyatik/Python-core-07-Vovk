'''Користувач вводить число, програма повинна вивести на екран його опис.
Наприклад, «додатне однозначне число», «від’ємне двозначне» тощо.'''

number = input('Input your number from -999 to 999: ')
sign = 'negative' if number[0] == '-' else 'positive'
number = int(number)
if number > -1000 and number < 1000:
    if number > -10 and number < 10:
        print('    Your number is', sign, 'one-digit')
    elif number < 100:
        print('    Your number is', sign, 'two-digit')
    else:
        print('    Your number is', sign, 'three-digit')
else:
    print('    The number must be greater than -1000 and less than 1000')