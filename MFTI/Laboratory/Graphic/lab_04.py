import graphics as gr

size_x = 800
size_y = 800

window = gr.GraphWin('Модель солнечной системы', size_x, size_y)

coords = gr.Point(400, 700)
speed = gr.Point(2, 0)
acceleration = gr.Point(0, 0)  # Ускорение


def add(point_1, point_2):  # point_1.x это coord_1.x с y то же самое в итоге мы здесь прибавляем координату к скорости
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)
    return new_point


def sub (point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)
    return new_point

def clear_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(size_x, size_y))
    rectangle.setFill('green')
    rectangle.draw(window)

    sun = gr.Circle(gr.Point(400, 400), 50)
    sun.setFill('yellow')
    sun.draw(window)


def draw_ball(coords):
    circle = gr.Circle(coords, 10)
    circle.setFill('red')
    circle.draw(window)
    return circle


# def check_coords(coords, speed):
#     if coords.x < 0 or coords.x > size_x:
#         speed.x = -speed.x
#
#     if coords.y < 0 or coords.y > size_y:
#         speed.y = -speed.y


def update_coords(coords, speed):
    return add(coords, speed)


def update_speed(speed, acceleration):
    return add(speed, acceleration)

def update_acceleration(ball_coords, center_coords):
    diff = sub(ball_coords, center_coords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3/2)
    G = 2000
    return gr.Point(-diff.x*G/distance_2, -diff.y*G/distance_2)

clear_window()
circle = draw_ball(coords)
diff_coords = coords

while True:
    acceleration = update_acceleration(coords, gr.Point(400, 400))
    coords = update_coords(coords, speed)
    speed = update_speed(speed, acceleration)
    # check_coords(coords, speed)
    circle.move(coords.x - diff_coords.x, coords.y - diff_coords.y)
    diff_coords = coords

    gr.time.sleep(0.001)