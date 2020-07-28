'''Користувач робить внесок в розмірі n гривень строком на years років
 під 10% річних (щороку розмір його внеску збільшується на 10%.
  Ці гроші додаються до суми вкладу, і на них в наступному році теж будуть відсотки).
  Написати функцію bank, яка приймає аргументи n і years,
  і повертає суму, яка буде на рахунку користувача.
'''

def bank(n, years):
    '''функція bank, приймає аргументи n - float і years - int,
    і повертає суму, яка буде на рахунку користувача.'''
    return n * (1 + 0.1)**years

def main():
    money = 0
    years = 0
    while True:
        n = input('Enter your money: ')
        if n.isdigit(): money = int(n)
        else:
            try:
                money = float(n)
            except:
                print('    Error: number of money must be an integer or a float!')
        if money > 0: break
    while True:
        n = input('Enter years: ')
        if n.isdigit(): years = int(n)
        else: print('    Error: number of money must be an integer or a float!')
        if years > 0: break

    sumMoney = bank(money, years)
    print(f'    The bank will pay you ${sumMoney:.2f} for {years} years')

if __name__ == "__main__":
    main()
