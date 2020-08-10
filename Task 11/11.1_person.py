'''. В класі Person визначте метод compare_age(), який повертатиме результат
    порівняння віку людини з Вашим віком. При заданих об’єктах p1, p2 і p3,
    які будуть ініціалізовані name та age, буде повертатися повідомлення наступного формату:
    {other_person} is {older than / younger than / the same age as} me.
'''


class Person():
    myAge = 41

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        if self.age < self.myAge:
            return f'{self.name} is younger than me.'
        elif self.age > self.myAge:
            return f'{self.name} is older than me.'
        else:
            return f'{self.name} is the same age as me.'


p1 = Person('Oleg', 45)
p2 = Person('Galina', 32)
p3 = Person('Olexander', 41)

print(p1)
print(p2)
print(p3)
