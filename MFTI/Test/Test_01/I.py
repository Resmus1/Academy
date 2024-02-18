'''
The sequence consists of natural numbers and ends with the number 0.
Determine the value of the largest element of the sequence.
'''
max = 0
n = -1
while n != 0:
    n = int(input())
    if n > max:
        max = n
print(max)
