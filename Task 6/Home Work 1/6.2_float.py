"""Заповнити список дійсними числами введенням з клавіатури.
Порахувати суму і добуток елементів списку.
Вивести на екран сам список, отримані суму і добуток його елементів.
"""
# check whether the entered number is correct
def check():
    while True:
        num = input('Input your number from: ')
        if '.' in num and num.count('.') == 1 and num[-1] != '.':
            return float(num)
        elif num.isalpha() and num.lower() == 's':
            return False
        else:
            print('    ERROR: your number must be a floating point number/'
                  '\n    or "S" to stop')

userList = []
elementList = True
while elementList:
    elementList = check()
    if elementList:
        userList.append(elementList)

sumList = sum(userList)
productList = 1
for i in userList:
    productList *= i

print()
print('%-30s' %'Your list:', userList)
print('%-31s%f' % ('The sum of the list items: ', sumList))
print('%-31s%f' % ('The product of the list items: ', productList))