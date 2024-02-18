# https://stepik.org/lesson/334152/step/4?unit=317561
def draw_triangle():
    """
    выводит звездный равнобедренный треугольник
    с основанием и высотой равными 15 и 8 соответственно:
    :return:
    """
    for i in range(8):
        print(' ' * (7 - i) + '*' * (1 + i * 2))


draw_triangle()
