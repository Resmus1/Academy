# https://stepik.org/lesson/352860/step/10?unit=336821
def check_char(test_char):
    """
    Тестирует символ из слова, на высоту и остольное убавляя лишнее по ANSI
    :param test_char:
    :return:
    """
    if test_char.isupper():
        if ord(test_char) + cnt_char > 90:
            return print(chr(156 - ord(test_char)), end='')  # 65 + 93
    if ord(test_char) + cnt_char > 122:
        return print(chr(219 - ord(test_char)), end='')  # 96 + 123
    else:
        return print(chr(ord(test_char) + cnt_char), end='')


text = 'Day, mice. "Year" is a mistake!'.split()

for word in text:
    cnt_char = 0
    for char in word:
        if char.isalpha():
            cnt_char += 1
    for char in word:
        if char.isalpha():
            check_char(char)
        else:
            print(char, end='')
    print(' ', end='')
