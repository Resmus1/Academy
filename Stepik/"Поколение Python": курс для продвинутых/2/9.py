# https://stepik.org/lesson/415554/step/9?unit=405083

coin_cut_p = input().split("О")
mx = 0

for el in coin_cut_p:
    mx = max(mx, el.count("Р"))

print(mx)
