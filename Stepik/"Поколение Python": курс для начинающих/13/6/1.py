# https://stepik.org/lesson/334314/step/3?unit=317733
def get_middle_point(x1, y1, x2, y2):
    '''
    Принимает в качестве аргументов координаты концов отрезка
    и возвращает координаты точки являющейся серединой данного отрезка.
    :return:
    '''
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return print(x, y)


x_1, y_1, x_2, y_2 = [int(input()) for i in range(4)]

get_middle_point(x_1, y_1, x_2, y_2)
