'''Вводяться десять натуральних чисел більше 2.
Порахувати, скільки серед них чисел, що кратні 5-ти.
'''
numberMultiples = 0
count = 0
while count < 10:
    numberUser = None
    while True:  # перевірка чи введене число користувача є натуральним і більше 2
        numberUser = input('Input your number: ')
        if numberUser.isdigit() and int(numberUser) > 2:
            numberUser = int(numberUser)
            break
        else:
            print('Sorry, your number must be an integer greater than 2')
    if numberUser % 5 == 0:
        count += 1
        numberMultiples += 1
    else:
        count += 1
print(f'There are "{count}" numbers which multiples of 5')
