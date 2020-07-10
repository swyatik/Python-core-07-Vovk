hours = ''
minutes = ''


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


# Запитуємо в користувача hours
# та перевіряємо його на відповідність (введені дані мають бути числом)
while True:
    string_input = input('Input hours: ')
    true, number_type = check_int_float(string_input)
    if true:
        if number_type == 'int':
            hours = int(string_input)
        else:
            hours = float(string_input)
        break
    else:
        print('   ERROR: Incorrect data entry. Must be a number greater than zero or zero....')

# Запитуємо в користувача height
while True:
    string_input = input('Input minutes: ')
    true, number_type = check_int_float(string_input)
    if true:
        if number_type == 'int':
            minutes = int(string_input)
        else:
            minutes = float(string_input)
        break
    else:
        print('   ERROR: Incorrect data entry. Must be a number greater than zero or zero....')

print('{} h. + {} m. = {} sec.'.format(hours, minutes, hours*3600 + minutes*60))
