
# Функція, що перевіряє чи рядок число int or float.
# Повертає tuple (true or false, тип даних в рядку)
def check_int_float(string):
    if string == '':
        return (False, '')
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


# Запитуємо в користувача number of animals
# та перевіряємо їх на відповідність (введені дані мають бути числом >=0)
def ask_and_check():
    number = None
    while True:
        string_input = input('Input number of the animals: ')
        true, number_type = check_int_float(string_input)
        if true:
            if number_type == 'int':
                number = int(string_input)
                break
            else:
                print('   ERROR: Incorrect data entry. Must be an integer greater than zero or zero....')
        else:
            print('   ERROR: Incorrect data entry. Must be an integer greater than zero or zero....')
    return number

print('How many chickens?')
chickens = ask_and_check()
print('How many cows?')
cows = ask_and_check()
print('How many pigs?')
pigs = ask_and_check()

total_number = chickens*2 + (cows + pigs)*4

print('The total number of legs: {}*2 + {}*4 + {}*4 = {}'.format(chickens, cows, pigs, total_number))
