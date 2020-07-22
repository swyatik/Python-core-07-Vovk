"""Вивести на екран «прямокутник», утворений з двох видів символів.
Контур прямокутника повинен складатися з одного символу,
 а "заливка" - з іншого.
"""
def check(side):
    while True:
        num = input(f"Input {side} of rectangle: ")
        if num.isdigit() and int(num) > 2:
            return int(num)
        else:
            print('ERROR: number must be an integer and greater than 2')

length = check('length')
width = check('width')

print(f"{' '*5}{'@'*length}")
for i in range(width - 2):
    print(f'{" "*5}@', end='')
    print(f'{"*"*(length-2)}', end='')
    print('@')
print('     ' + '@'*length)

