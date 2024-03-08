# https://stepik.org/lesson/415554/step/6?unit=405083

size = int(input())
seq = [int(input()) for _ in range(size)]
number = int(input())
flag = False

for i in range(size):
    for j in range(size):
        if i != j and seq[i] * seq[j] == number:
            flag = True

if flag:
    print("ДА")
else:
    print("НЕТ")
