# https://stepik.org/lesson/415554/step/8?unit=405083

options = ["камень", "ящерица", "Спок", "ножницы", "бумага"]
score = options.index(input()) - options.index(input())
if score in (2, 4, -1, -3):
    print('Тимур')
elif score in (1, 3, -2, -4):
    print('Руслан')
else:
    print('ничья')
