
# Функція, що перевіряє чи рядок число int or float.
# Повертає tuple (true or false, тип даних в рядку)
def check_int_float(string):
    if string == '':
        return (True, 'int')
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


# Запитуємо в користувача число
# та перевіряємо його на відповідність (введені дані мають бути числом >=0)
def ask_and_check():
    number = None
    while True:
        string_input = input('Input number: ')
        true, number_type = check_int_float(string_input)
        if true:
            if number_type == 'int':
                if string_input == '':
                    number = 0
                else:
                    number = int(string_input)
                break
            else:
                print('   ERROR: Incorrect data entry. Must be an integer greater than zero or zero....')
        else:
            print('   ERROR: Incorrect data entry. Must be an integer greater than zero or zero....')
    return number

print('How many wins?')
wins = ask_and_check()
print('How many draws?')
draws = ask_and_check()
print('How many losses?')
losses = ask_and_check()

number_of_points = wins*3 + draws

print('The number of points a football team: {}*3 + {}*1 + {}*0 = {}'.format(wins, draws, losses, number_of_points))
