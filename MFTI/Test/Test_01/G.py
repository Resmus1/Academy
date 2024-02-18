'''
Determine the sum of all the elements of the sequence ending with the number 0.
'''
n = int(input())
count = 0
while n != 0:
    count += n
    n = int(input())
print(count)
