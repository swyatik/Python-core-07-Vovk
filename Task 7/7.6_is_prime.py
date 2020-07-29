"""Написати функцію is_prime, яка приймає 1 аргумент - число від 0 до 1000,
 і повертає True, якщо воно просте, і False - в іншому випадку.
"""

def is_prime(number):
    """функція is_prime, приймає 1 аргумент - число від 0 до 1000,
    і повертає True, якщо воно просте, і False - в іншому випадку."""
    if 0 <= number <= 1000:
        if number % 2 == 0:
            return number == 2
        divider = 3
        while divider * divider <= number and number % divider != 0:
            divider += 2
        return divider * divider > number
    else:
        return False

def main():
    while True:
        num = input("Enter your number (>= 0 and <= 1000): ")
        if num.isdigit():
            if is_prime(int(num)):
                print(f"    The number {num} is prime!")
            else:
                print(f"    The number {num} does not prime!")
            break
        else:
            print("    Error: your number must be an integer >0 <1000! Try again.")

if __name__ == "__main__":
    main()
