width = ''
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


# Запитуємо в користувача width
while True:
    string_input = input('Input width of rectangle: ')
    true, number_type = check_int_float(string_input)
    if true:
        if number_type == 'int':
            width = int(string_input)
        else:
            width = float(string_input)
        break
    else:
        print('   ERROR: Incorrect data entry. Must be a number greater than zero....')

# Запитуємо в користувача height
while True:
    string_input = input('Input height of rectangle: ')
    true, number_type = check_int_float(string_input)
    if true:
        if number_type == 'int':
            height = int(string_input)
        else:
            height = float(string_input)
        break
    else:
        print('   ERROR: Incorrect data entry. Must be a number greater than zero....')

print('Perimeter of rectangle: {}*2 + {}*2 = {}'.format(width, height, width*2 + height*2))
