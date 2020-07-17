number = 1234
strNumber = str(number)
product = int(strNumber[0]) * int(strNumber[1]) * int(strNumber[2]) * int(strNumber[3])
reversNumber = int(strNumber[::-1])
print('Product of number %d is %15d' % (number, product))
print('Inverse number to number %d is %8d' % (number, reversNumber))