import graphics as gr

window = gr.GraphWin("Картина", 1000, 900)


def bacground_up():
    """
    Рисует небо.
    :return:
    """
    bg_up = gr.Rectangle(gr.Point(0, 0), gr.Point(1000, 900))
    bg_up.setFill('blue')

    bg_up.draw(window)


def sun(x_sun, y_sun):
    """
    Рисует солнце, задается параметр положения.
    :return:
    """
    sn = gr.Circle(gr.Point(x_sun, y_sun), 50)
    sn.setFill('yellow')
    sn.setOutline('yellow')

    sn.draw(window)


def cloud(x_cloud, y_cloud):
    """
    Рисует облако, задается параметр положения.
    :return:
    """
    cl1 = gr.Circle(gr.Point(x_cloud, y_cloud), 30)
    cl1.setFill('white')
    cl1.setOutline('white')
    cl2 = gr.Circle(gr.Point(x_cloud + 20, y_cloud - 20), 30)
    cl2.setFill('white')
    cl2.setOutline('white')
    cl3 = gr.Circle(gr.Point(x_cloud + 40, y_cloud + 20), 30)
    cl3.setFill('white')
    cl3.setOutline('white')
    cl4 = gr.Circle(gr.Point(x_cloud + 70, y_cloud - 10), 30)
    cl4.setFill('white')
    cl4.setOutline('white')
    cl5 = gr.Circle(gr.Point(x_cloud + 90, y_cloud + 10), 30)
    cl5.setFill('white')
    cl5.setOutline('white')

    cl1.draw(window)
    cl2.draw(window)
    cl3.draw(window)
    cl4.draw(window)
    cl5.draw(window)


def background_down():
    """
    Рисует землю.
    :return:
    """
    bg_d = gr.Rectangle(gr.Point(0, 500), gr.Point(1000, 900))
    bg_d.setFill('brown')

    bg_d.draw(window)


def three(x_three, y_three):
    """
    Рисует дерево, задается параметр положения.
    :return:
    """
    # Ствол
    trunk = gr.Rectangle(gr.Point(x_three, y_three), gr.Point(x_three + 50, y_three - 110))
    trunk.setFill('chocolate')

    # Листва
    foliage1 = gr.Polygon(gr.Point(x_three - 100, y_three - 110), gr.Point(x_three + 150, y_three - 110),
                          gr.Point(x_three + 25, y_three - 200))
    foliage1.setFill('green')
    foliage1.setWidth(5)
    foliage2 = gr.Polygon(gr.Point(x_three - 100, y_three - 170), gr.Point(x_three + 150, y_three - 170),
                          gr.Point(x_three + 25, y_three - 300))
    foliage2.setFill('green')
    foliage2.setWidth(5)
    foliage3 = gr.Polygon(gr.Point(x_three - 100, y_three - 250), gr.Point(x_three + 150, y_three - 250),
                          gr.Point(x_three + 25, y_three - 400))
    foliage3.setFill('green')
    foliage3.setWidth(5)

    trunk.draw(window)
    foliage1.draw(window)
    foliage2.draw(window)
    foliage3.draw(window)


def windows(x_home, y_home):
    """
    Рисует окно, можно задать параметры расположения окна относительно основной точки дома.
    :return:
    """
    # Рама
    win = gr.Rectangle(gr.Point(x_home + 50, y_home - 220), gr.Point(x_home + 120, y_home - 120))
    win.setFill('white')
    win.setWidth(5)

    # Рейка
    rail = gr.Polygon(gr.Point(x_home + 85, y_home - 220), gr.Point(x_home + 85, y_home - 120))
    rail.setWidth(3)

    win.draw(window)
    rail.draw(window)


def home(x_home, y_home):
    """
    Рисует домик: основание, стены, окна, крышу, дверь. Задаются параметры относительно основной точки.
    :return:
    """
    # Основание
    base = gr.Rectangle(gr.Point(x_home, y_home), gr.Point(x_home + 450, y_home + 50))
    base.setFill('black')

    # Стены
    wall = gr.Rectangle(gr.Point(x_home + 20, y_home - 300), gr.Point(x_home + 430, y_home))
    wall.setFill('grey')
    wall.setOutline('grey')

    # Крыша
    roof = gr.Polygon(gr.Point(x_home + 20, y_home - 300), gr.Point(x_home + 430, y_home - 300),
                      gr.Point(x_home + 200, y_home - 500))
    roof.setFill('green')
    roof.setWidth(3)

    # Дверь
    door = gr.Rectangle(gr.Point(x_home + 320, y_home), gr.Point(x_home + 400, y_home - 150))
    door.setFill('tan')

    # Ручка
    handle = gr.Circle(gr.Point(x_home + 385, y_home - 65), 10)
    handle.setFill('black')

    base.draw(window)
    wall.draw(window)
    roof.draw(window)
    door.draw(window)
    handle.draw(window)
    windows(x_home, y_home)
    windows(x_home + 165, y_home)


def sky(x_sun=920, y_sun=70, cloud1_x=550, cloud1_y=150,
        cloud2_x=100, cloud2_y=200, cloud3_x=800, cloud3_y=120):
    """
    Рисует небо, облака и солнце. Указаны стандартные положения X, Y.
    :param x_sun: X Положение Солнца
    :param y_sun: Y Положение Солнца
    :param cloud1_x: X Положение Облака № 1
    :param cloud1_y: с Облака № 1
    :param cloud2_x: X Положение Облака № 2
    :param cloud2_y: Y Положение Облака № 2
    :param cloud3_x: X Положение Облака № 3
    :param cloud3_y: Y Положение Облака № 3
    :return:
    """
    bacground_up()
    sun(x_sun, y_sun)
    cloud(cloud1_x, cloud1_y)
    cloud(cloud2_x, cloud2_y)
    cloud(cloud3_x, cloud3_y)


def earth(x_three=700, y_three=580, x_home=100, y_home=600):
    """
    Рисует Землю, домик, дерево. Указаны стандартные положения X, Y.
    :param x_three: X Положение Дерева
    :param y_three: Y Положение Дерева
    :param x_home: X Положение Дома
    :param y_home: Y Положение Дома
    :return:
    """
    background_down()
    three(x_three, y_three)
    home(x_home, y_home)


sky()
earth()

window.getMouse()
window.close()
