# https://stepik.org/lesson/415554/step/7?unit=405083

options = ["камень", "ножницы", "бумага"]
results = ["ничья", "Руслан", "Тимур"]

timur_move, ruslan_move = input(), input()

case = options.index(timur_move) - options.index(ruslan_move)

print(results[case])
