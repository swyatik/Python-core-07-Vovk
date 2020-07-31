"""Задано n рядочків символів.
    Розробити програму, яка визначає і друкує окремо приголосні
     та голосні малі літери латинського алфавіту, які є в кожному рядку.
"""
def main():
    while True:
        try:
            n = int(input("Enter the number of lines: "))
            break
        except:
            print(f'{" "*4} Error: the number of lines must be an integer!')

    userList = [[] for i in range(n)]
    for i in range(n):
        userList[i].append(input(f'Enter your line {i+1}: '))

    vowelsLower = {'a', 'e', 'i', 'o', 'u', 'y'}
    consonantsLower = set([chr(i) for i in range(97, 123)]).difference(vowelsLower)

    print()
    for i in range(n):
        tempSet = set(userList[i][0])
        print(f"The {i+1} line \"{userList[i][0]}\" contains:")
        print(f"{' '*4}{'small vowels:':20s}{tempSet.intersection(vowelsLower)}")
        print(f"{' '*4}{'small consonants:':20s}{tempSet.intersection(consonantsLower)}")

if __name__ == "__main__":
    main()