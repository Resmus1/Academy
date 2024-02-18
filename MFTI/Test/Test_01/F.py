'''
The program receives a sequence of non-negative integers as input, each number is written in a separate line.
The sequence ends with the number 0, when reading which the program must finish its work
and output the number of members of the sequence (not counting the final number 0).
The numbers following the number 0 do not need to be read.
'''
n = int(input())
count = 0
while n != 0:
    count += 1
    n = int(input())
print(count)
