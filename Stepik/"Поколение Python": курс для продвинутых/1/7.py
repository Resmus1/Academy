# https://stepik.org/lesson/415553/step/8?unit=405082

n = list(input())
new_n = ""

while len(n) >= 3:
    new_n += n.pop(-1) + n.pop(-1) + n.pop(-1) + ','
new_n += ''.join(n[::-1])
print(new_n[::-1].lstrip(','))
