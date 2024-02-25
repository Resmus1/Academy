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
            if turn > lang[1] - 1:
                print(f"Введите число не более {lang[1] - 1} шага")
            else:
                return turn
        except ValueError:
            print('Ошибка! Введите цифры\n')


def decryption(word, text, lang, dec_rotate):
    for char in text:
        if char.isalpha():
            if ord(char) - (dec_rotate + 1) < (lang[0] - (lang[1])):
                word += chr(lang[0] - (dec_rotate - (ord(char) - (lang[0] - (lang[1])))))
            else:
                word += chr(ord(char) - dec_rotate)
        else:
            word += char
    return word


def encryption(word, text, lang, enc_rotate):
    for char in text:
        if char.isalpha():
            if ord(char) + enc_rotate > lang[0]:
                word += chr(ord(char) - (lang[1] - enc_rotate))
            else:
                word += chr(ord(char) + enc_rotate)
        else:
            word += char
    return word


def crypt(text, style, lang, crypt_rotate):
    word = ''
    if style == 'decryption':
        return decryption(word, text, lang, crypt_rotate).capitalize()
    elif style == 'encryption':
        return encryption(word, text, lang, crypt_rotate).capitalize()


def brute(text, style, brute_lang_choice, brute_rotate):
    while True:
        go_brute = input('Проходим от 1-го до последнего шага? (Yes / No)\n').lower()
        if go_brute in ('yes', 'no'):
            if go_brute == 'yes':
                brute_rotate += 1
                for i in range(0, brute_rotate):
                    print(f'{i}) {crypt(text, style, brute_lang_choice, i)}')
                    brute_rotate -=1
                    if brute_rotate == 0:
                        return
            else:
                return print(crypt(text, style, brute_lang_choice, brute_rotate))
        else:
            print("Вы ввели неверный ответ.")


# Нужно сделать надстройку для брута

input_text = input("Введите текст\n> ").lower()
input_style = style_code()
input_lang_choice = lang_choice()
input_rotate = rotate(input_lang_choice)

brute(input_text, input_style, input_lang_choice, input_rotate)
