from random import randint

def main():
    synonims = {'beautiful': ['pretty', 'charming'],\
                'warm': ['hot', 'friendly'],\
                'kind': ['good', 'well'],\
                'magic': ['fairy', 'imaginary'],\
                'nice': ['pleasant', 'fine'],\
                'modest': ['descreet']}

    word = input('Enter a word: ')
    # Якщо слово є в словнику друкуємо його синоніми
    if word in synonims:
        print(f'Synonyms for "{word}" are: ', end='')
        for i in range(len(synonims[word])):
            print(synonims[word][i], end='')
            if i != len(synonims[word]) - 1:
                print(', ', end='')
    else: print('    Sorry, but there is not such a word in dictionary! Try again.')
    print()

    sentence = input('Enter a sentence: ')
    lengtSent = len(sentence)
    for key in synonims:
        index = sentence.find(key)
        # Замінюємо слово доки воно є в реченні
        while index >= 0:
            if index + len(key) == lengtSent:
                sentence = sentence.replace(key, synonims[key][randint(0, len(synonims[key]) - 1)])
                break
            # Перевірка чи слово повне чи тільки частина іншого слова
            # наприклад: шукаємо 'kind', а в реченні- 'kindly'
            # тому дивимось чи після слова 'kind' маленька літера, якщо ні то замінюємо на синонім
            elif not (sentence[index + len(key)].isalpha() and sentence[index + len(key)].islower()):
                sentence = sentence.replace(key, synonims[key][randint(0, len(synonims[key])-1)])
            index = sentence[index + len(key)].find(key)
    print(sentence)


if __name__ == "__main__":
    main()