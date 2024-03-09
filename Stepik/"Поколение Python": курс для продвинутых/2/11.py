# https://stepik.org/lesson/415554/step/11?unit=405083

text = f'{input()} запретил букву'
i = 0

while text:
    while chr(1072 + i) in text:
        print(text, chr(1072 + i))
        text = text.replace(chr(1072 + i), '').strip()
    i += 1
