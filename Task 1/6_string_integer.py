string_in = ''


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


# Запитуємо в користувача ввести рядок
# Перевіряємо його та конвертуємо
while True:
    string_input = input('Input your a string: ')
    true, number_type = check_number(string_input)
    if true:
        if number_type == 'int':
            string_in = int(string_input)
        else:
            print('    Your a string is a float')
            print('    Do you want to convert a float in an integer?')
            while True:
                answer = input('Y - yes, N - no: ')
                if answer.isalpha() and len(answer) == 1 and (answer.lower() == 'y' or answer.lower() == 'n'):
                    if answer.lower() == 'y':
                        string_in = int(float(string_input))
                    else:
                        string_in = '-'
                    break
        break
    else:
        print("   This string can't to be to convert in an integer")

print('string: "{}" = integer: {}'.format(string_input, string_in))
