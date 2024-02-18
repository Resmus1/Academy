# For a given natural number N , print the smallest integer k such that 2^k >= N .
n = int(input())
k = 0
while n > 0:
    k += 1
    n = n // 2
print(k)