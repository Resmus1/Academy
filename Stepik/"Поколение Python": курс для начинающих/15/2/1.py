# https://stepik.org/lesson/352860/step/10?unit=336821
def shift_char(test_char, cnt_char):
    """
    Тестирует символ из слова, на высоту и остольное убавляя лишнее по ANSI
    """
    if test_char.isupper():
        base = 65
    else:
        base = 97

    shifted = ord(test_char) + cnt_char - base
    print(chr(base + (shifted % 26)), end='')


text = input().split()

for word in text:
    cnt_char = sum(1 for char in word if char.isalpha())
    for char in word:
        if char.isalpha():
            shift_char(char, cnt_char)
        else:
            print(char, end='')
    print(' ', end='')
