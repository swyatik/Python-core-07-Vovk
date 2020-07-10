base = ''
height = ''


# Функція, що перевіряє чи рядок число int or float.
# Повертає tuple (true or false, тип даних в рядку)
def check_int_float(string):
    if string[0] == '-':
        return (False, '')
    if string.isdigit():
        return (True, 'int')
    else:
        try:
            float(string)
            return (True, 'float')
        except:
            return (False, '')


# Запитуємо в користувача base
while True:
    string_input = input('Input your base: ')
    true, number_type = check_int_float(string_input)
    if true:
        if number_type == 'int':
            base = int(string_input)
        else:
            base = float(string_input)
        break
    else:
        print('   The data entered is not a number...')

# Запитуємо в користувача heght
while True:
    string_input = input('Input your height: ')
    true, number_type = check_int_float(string_input)
    if true:
        if number_type == 'int':
            height = int(string_input)
        else:
            height = float(string_input)
        break
    else:
        print('   The data entered is not a number...')

print('Area of triangle: {} * {} /2 = {}'.format(base, height, base * height / 2))
