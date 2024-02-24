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


def check_num():
    while True:
        try:
            return int(input("Введите количество шагов в кодировке\n> "))
        except ValueError:
            print('Ошибка! Введите цифры\n')


def crypt(text, style, lang, rotate):
    word = ''
    if style == 'decryption':
        for char in text:
            if char.isalpha():
                if ord(char) - rotate < (lang[0] - (lang[1])):
                    word += chr(lang[0]-(rotate-(ord(char) - (lang[0] - (lang[1])))))
                else:
                    word += chr(ord(char) - rotate)
            else:
                word += char
    elif style == 'encryption':
        for char in text:
            if char.isalpha():
                if ord(char) + rotate > lang[0]:
                    word += chr(ord(char) - (lang[1] - rotate))
                else:
                    word += chr(ord(char) + rotate)
            else:
                word += char
    return word.capitalize()


# print(crypt(input("Введите текст\n> ").lower(), style_code(), lang_choice(), check_num()))

# Нужно оптимизироват крипт
# Нужно сделать надстройку для брута
for i in range(0, 25):
    print(i)
    print(crypt("Hawnj pk swhg xabkna ukq nqj.".lower(), 'encryption', (122, 26), i))