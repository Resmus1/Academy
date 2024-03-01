# https://stepik.org/lesson/415553/step/10

n, k = int(input()), int(input())

list_n = [i for i in range(1, n + 1)]

while len(list_n) > 1:
    for i in range(k-1):
        list_n.append(list_n.pop(0))
        if i == len(list_n):
            i = 0
    del list_n[0]
print(list_n[0])
