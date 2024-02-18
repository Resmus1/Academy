'''
Count the number of even elements in an array of integers ending in zero.
Zero itself should not be taken into account.
'''
count = 0
n = -1
while n != 0:
    if n % 2 == 0:
        count += 1
    n = int(input())
print(count)
