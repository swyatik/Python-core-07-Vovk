from random import randint

m = int(input("Input M (M>3): "))  # row
n = int(input("Input N (N>2): "))  # columns

numbers = [[] for i in range(m)]
print(f'{"_"*5*n}\nOur list:')
for i in numbers:
    for j in range(n):
        i.append(randint(1, 100))
        print("%4d " % i[j], end="")
    print()

numbersForMax = [i[1] for i in numbers]  # list 2-column
print(f'{"_"*5*n}')
print("min of 3rd row:    %4d" % min(numbers[2]))
print("max of 2rd column: %4d" % max(numbersForMax))




