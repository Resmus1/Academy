# https://stepik.org/lesson/415554/step/10?unit=405083

n = int(input())
for i in range(n):
    seq = ["a", "n", "t", "o", "n"]
    s = list(input())

    while seq and s:
        if seq[0] == s[0]:
            seq.pop(0)
            s.pop(0)
        else:
            s.pop(0)

    if not seq:
        print(i + 1, end=" ")