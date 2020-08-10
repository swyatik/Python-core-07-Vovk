'''В класі Name визначте:
    атрибути для first name та last name (fname та lname відповідно);
    атрибут fullname що повертає first і last names;
    атрибут initials який повертає ініціали (перші літери first та last name, розділених ‘.’
'''

class Name():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.fullname = f'{self.fname} {self.lname}'
        self.initials = f'{self.fname[0]}.{self.lname[0]}'

person = Name('Will', 'Smith')
print(f'{"Actor:":10s}{person.fullname}')
print(f'{"Initials:":10s}{person.initials}')
