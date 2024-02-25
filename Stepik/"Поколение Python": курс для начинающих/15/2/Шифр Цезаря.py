# https://stepik.org/lesson/352860/step/4?unit=336821
def style_code():
    actions = {'1': 'encryption', '2': 'decryption'}
    while True:
        code = input("Выберите действие\n1) Зашифровать\n2) Расшифровать\n> ")
        if code in actions:
            return actions[code]


def lang_choice():
    languages = {'1': (122, 26), '2': (1103, 32)}
    while True:
        lang = input("Выберите язык\n1) Английский\n2) Русский\n> ")
        if lang in languages:
            return languages[lang]


def rotate(lang):
    while True:
        try:
            turn = int(input("Введите количество шагов в кодировке\n> "))
            if turn > lang[1]-1:
                print(f"Введите число не более {lang[1]-1} шага")
            else:
                return turn
        except ValueError:
            print('Ошибка! Введите цифры\n')


def decryption(word, text, lang, rotate):
    for char in text:
        if char.isalpha():
            if ord(char) - rotate < (lang[0] - (lang[1])):
                word += chr(lang[0] - (rotate - (ord(char) - (lang[0] - (lang[1])))))  # Нужно исправить, в аншлиской расшифровке попадает на символ а не букву!
            else:
                word += chr(ord(char) - rotate)
        else:
            word += char
    return word


def encryption(word, text, lang, rotate):
    for char in text:
        if char.isalpha():
            if ord(char) + rotate > lang[0]:
                word += chr(ord(char) - (lang[1] - rotate))
            else:
                word += chr(ord(char) + rotate)
        else:
            word += char
    return word


def crypt(text, style, lang, rotate):
    word = ''
    if style == 'decryption':
        return decryption(word, text, lang, rotate).capitalize()
    elif style == 'encryption':
        return encryption(word, text, lang, rotate).capitalize()


def brute(text, style, lang_choice, rotate):
    while True:
        go_brute = input('Проходим от 1-го до последнего шага? (Yes / No)\n').lower()
        if go_brute in ('yes', 'no'):
            if go_brute == 'yes':
                for i in range(0, rotate + 1):
                    print(f'{i}) {crypt(text, style, lang_choice, i)}')
            else:
                return print(crypt(text, style, lang_choice, rotate))
        else:
            print("Вы ввели неверный ответ.")


# Нужно сделать надстройку для брута

text = input("Введите текст\n> ").lower()
style = style_code()
lang_choice = lang_choice()
rotate = rotate(lang_choice)

brute(text, style, lang_choice, rotate)
