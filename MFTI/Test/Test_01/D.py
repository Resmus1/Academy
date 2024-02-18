"""For a given natural number N, print out all squares of natural
numbers not exceeding N in ascending order."""
n = int(input())
x = 1
while x ** 2 <= n:
    print(x ** 2)
    x += 1
