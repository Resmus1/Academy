# https://stepik.org/lesson/334314/step/5?unit=317733
from math import sqrt


def solve(a, b, c):
    """
    принимает в качестве аргументов три целых числа a, b, c – коэффициенты квадратного уравнения
    и возвращает его корни в порядке возрастания.
    :return:
    """
    d = b ** 2 - (4 * a * c)
    x_1 = (-b + sqrt(d)) / (2 * a)
    x_2 = (-b - sqrt(d)) / (2 * a)
    return print(min(x_1, x_2), max(x_1, x_2))


a, b, c = [int(input()) for i in range(3)]
solve(a, b, c)
