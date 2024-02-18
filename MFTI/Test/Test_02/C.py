count = int(input())
temp = 0
result = 0
for _ in range(count):
    x = int(input())
    if x == 1:
        temp += 1
    else:
        result = max(result, temp)
        temp = 0
print(max(result, temp))
