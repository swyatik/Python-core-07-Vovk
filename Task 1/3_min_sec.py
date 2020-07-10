number_1 = ''


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


# Функція, що перевіряє чи є знак '-' в рядку,
# якщо є то передає в check_int_float рядок без першого знаку '-'
# Повертає результат функції check_int_float
def check_number(string):
    if string[0] == '-':
        if string.count('-') > 1:
            check_num = check_int_float(string)
        else:
            check_num = check_int_float(string[1:])
    else:
        check_num = check_int_float(string)
    return check_num


# Запитуємо в користувача minutes
while True:
    string_input = input('Input your minutes: ')
    true, number_type = check_number(string_input)
    if true:
        if number_type == 'int':
            number_1 = int(string_input)
        else:
            number_1 = float(string_input)
        break
    else:
        print('   The data entered is not a number...')

print('{} min. = {} sec.'.format(number_1, int(number_1 * 60)))
