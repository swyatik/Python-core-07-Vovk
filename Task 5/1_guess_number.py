'''У програмі генерується випадкове ціле число від 0 до 100.
Користувач повинен його відгадати не більше ніж за 10 спроб.
Після кожної невдалої спроби повинно повідомлятися чи більше
чи менше введене користувачем число, ніж те, що загадане.
Якщо за 10 спроб число не відгадане, то вивести загадане число.
'''

from random import randint

randomNumber = randint(0, 100)
count = 0
print("Hi there! \nThis game is called \"guess the number\". \nYou have ten attempts to guess the intended number from 0 to 100. \nFollow the prompts. \nGood luck!")
while count < 10:
    numberUser = None
    while True:  # перевірка чи введене число користувача є цілим та в межах допуску
        numberUser = input('Input your number: ')
        if numberUser.isdigit() and -1 < int(numberUser) <= 100:
            numberUser = int(numberUser)
            break
        else:
            print('Sorry, your number must be an integer equal or more than 0 and less than 100!')
    if numberUser == randomNumber:
        print("***WIN!***")
        break
    elif numberUser < randomNumber:
        print('Your number is less than expected.')
        count += 1
    else:
        print('Your number is more than expected.')

else:
    print('***FAIL!***')