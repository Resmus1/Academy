'''
The sequence consists of natural numbers and ends with the number 0.
In total, no more than 10,000 numbers are entered (not counting the final number 0).
Determine how many elements of this sequence are equal to its largest element.
The numbers following the number 0 do not need to be read.
'''
l = []
n = -1
while n != 0: n = int(input()); l.append(n)
print(l.count(max(l)))
