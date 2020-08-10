'''Визначте атрибути fullname та email в класі Employee. При заданих first та last names:
    - В конструкторі сформуйте fullname звичайним з’єднанням через пробіл first та last name.
    В конструкторі сформуйте email з’єднанням first та last name через ‘.’ між ними та приєднуючи
    ‘@company.com’ наприкінці.
'''


class Employee():
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.fullname = f'{self.firstName} {self.lastName}'
        self.email = f'{self.firstName.lower()}.{self.lastName.lower()}@company.com'


person = Employee('Moby', 'Dick')

print(f'{"Full name:":10s} {person.fullname}')
print(f'{"Email:":>10s} {person.email}')