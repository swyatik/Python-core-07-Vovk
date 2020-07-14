'''Відомий РІК. Визначити, чи буде цей рік високосним,
і до якого століття цей рік відноситься.
'''
year = int(input('Input the year: '))
century = year // 100
if year % 4 == 0:
    print("%d is a high year. This is the %dth century." % (year, century))
else:
    print("%d is not a high year. This is the %dth century." % (year, century))
