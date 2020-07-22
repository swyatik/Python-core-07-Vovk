'''Вивести на екран таблицю множення (від 1 до 9).
'''

count = 1
while count < 10:
    for i in range(1, 10):
        print('     %d * %d = %2d' % (count, i, count * i), end='    ')
        print('%d * %d = %2d' % (count + 1, i, (count + 1) * i), end='    ')
        print('%d * %d = %2d' % (count + 2, i, (count + 2) * i))
    print()
    count += 3
