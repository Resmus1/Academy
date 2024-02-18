# https://stepik.org/lesson/334152/step/6?unit=317561
from math import factorial
def compute_binom(n, k):
    '''
    Принимает в качестве аргументов два натуральных числа и возвращает значение.
    :return:
    '''
    return print(int(factorial(n)/ (factorial(k) * factorial(n - k))))


compute_binom(int(input()), int(input()))