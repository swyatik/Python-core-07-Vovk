"""Створіть словник, зв'язавши його з змінною school,
    і наповніть його даними, які б відображали кількість учнів в десяти різних класах
    (наприклад, 1а, 1б, 2б, 6а, 7в тощо.). Дізнайтеся скільки людей в певному класі.
    Уявіть, що в школі відбулися зміни, додайте їх в словник:
    - В трьох класах змінилося кількість учнів;
    - В школі з'явилося два нових класу;
    - В школі розформували один з класів.
    Виведіть вміст словника на екран."""

from random import randint

def main():
    school = {"1a": 7, "1b": 27, "2a": 30, "2b": 20, "3a": 22, "7b": 33, "8a": 23, "9a": 18, "9b": 21, "10b": 26}
    # Запитуємо в користувача номер класу і виводимо кількість учнів.
    while True:
        ask = input("Enter the class number or '00' to exit:\n")
        if ask == "00":
            break
        else:
            number = school.get(ask, False)
            if not number:
                print(f"{' '*4}There is no '{ask}' class in our school.")
            else:
                print(f"{' '*4}There are {school[ask]} students in the '{ask}' class")

    school["1b"], school["2b"], school["8a"] = 34, 25, 30
    school["10a"], school["3b"] = 22, 15
    school.pop("1a")
    for key in school:
        print(f"There are {school[key]} students in {key:>3s} class.")

if __name__ == "__main__":
    main()