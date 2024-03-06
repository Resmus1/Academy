# https://stepik.org/lesson/415554/step/1?unit=405083

list_xy = []
part = {"Первая четверть": 0,
        "Вторая четверть": 0,
        "Третья четверть": 0,
        "Четвертая четверть": 0,
        }

[list_xy.append([int(i) for i in input().split()]) for _ in range(int(input()))]

for i in list_xy:
    x, y = i[0], i[1]
    if 0 in i:
        pass
    elif x > 0 < y:
        part["Первая четверть"] += 1
    elif x < 0 < y:
        part["Вторая четверть"] += 1
    elif x < 0 > y:
        part["Третья четверть"] += 1
    elif x > 0 > y:
        part["Четвертая четверть"] += 1

[print(f"{key}: {value}") for key, value in part.items()]
