# https://stepik.org/lesson/313439/step/6?unit=295959

n, text = int(input()), input()
for char in text:
    if (i := (ord(char) - n)) < 97:
        print(chr(122 - (96 - i)), end='')
    else:
        print(chr(ord(char) - n), end='')
