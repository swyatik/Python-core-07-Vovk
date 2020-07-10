number = ''
exponent = ''


# Функція, що перевіряє чи рядок число int or float.
# Повертає tuple (true or false, тип даних в рядку)
def check_int_float(string):
    if string.isdigit():
        return (True, 'int')
    else:
        try:
            float(string)
            return (True, 'float')
        except:
            return (False, '')


# Запитуємо в користувача number
# та перевіряємо його на відповідність (введені дані мають бути числом)
while True:
    string_input = input('Input width of rectangle: ')
    true, number_type = check_int_float(string_input)
    if true:
        if number_type == 'int':
            number = int(string_input)
        else:
            number = float(string_input)
        break
    else:
        print('   ERROR: Incorrect data entry. Must be a number...')

# Запитуємо в користувача exponent
# та перевіряємо його на відповідність (введені дані мають бути числом)
while True:
    string_input = input('Input height of rectangle: ')
    true, number_type = check_int_float(string_input)
    if true:
        if number_type == 'int':
            exponent = int(string_input)
        else:
            exponent = float(string_input)
        break
    else:
        print('   ERROR: Incorrect data entry. Must be a number...')

print('Power: {} ** {} = {}'.format(number, exponent, number ** exponent))
