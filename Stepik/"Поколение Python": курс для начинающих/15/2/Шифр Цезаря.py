# https://stepik.org/lesson/352860/step/4?unit=336821

# direction = ('encryption', 'decryption')
# language = {'eng': [122, 26], 'rus': [1103, 32]}
# input_rotate = 10
# input_text = 'Блажен, кто верует, тепло ему на свете!'.lower()
setting = {'direction': 1, 'language': {'eng': [122, 26], 'rus': [1103, 32]}, 'input_rotate': 0, 'input_text': ''}

def setting_encrypt():
    """
    Записать в функцию параметры из настроек, совместить по параметрам с генератором паролей
    """


def crypt(text, max_symbol, max_letter, rotate):
    word = ''
    for i in text:
        if ord(i) + rotate > max_symbol:
            word += chr((ord(i) - (max_letter - rotate)))
        elif i in (' ', '?', '!', ',', '.'):
            word += i
        else:
            word += chr(ord(i) + rotate)
    return word.capitalize()


print(crypt(input_text, language['rus'][0], language['rus'][1], input_rotate))
