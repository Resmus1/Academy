# https://stepik.org/lesson/334314/step/4?unit=317733
from math import pi


def get_circle(radius):
    """
    Принимает в качестве аргумента радиус окружности и возвращает два значения:
    длину окружности и площадь круга.
    :return:
    """
    length = 2 * pi * radius
    square = pi * radius ** 2
    return print(length, square)


get_circle(float(input()))
