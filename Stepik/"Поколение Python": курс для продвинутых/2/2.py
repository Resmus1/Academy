# https://stepik.org/lesson/415554/step/2?unit=405083

diff = 0
numbers = list(map(int, input().split()))

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        diff += 1
print(diff)
