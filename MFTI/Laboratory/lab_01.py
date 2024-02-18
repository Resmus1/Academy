import turtle as t

# import math


# def symbolS (length=t.numinput("Symbol \'S\'", "Enter lenght 10-100:", 50, minval=10, maxval=100)):
#     """
#     :return: Draw symbol S
#     """
#     for i in range(3):
#         t.fd(length)
#         t.lt(90)
#     t.seth(90)
#     for i in range(2):
#         t.fd(length)
#         t.rt(90)

# def square(length):
#     """
#     :return: Draw square
#     """
#     for _ in range(4):
#         t.fd(length)
#         t.lt(90)

# def circle(size=t.numinput("Circle", "Enter size 5-30:", 5, minval=5, maxval=30)):
#     """
#     :return: draw circle
#     """
#     for _ in range(36):
#         t.fd(size)
#         t.lt(10)

# def spider(legs=int(t.numinput("Count legs", "Enter count legs 2-100", 2, minval=2, maxval=100))):
#     """
#     :return: draw lines
#     """
#     for _ in range(legs):
#         t.rt(360/legs)
#         t.fd(100)
#         t.stamp()
#         t.rt(180)
#         t.fd(100)
#         t.rt(180)

# def spiral(
#         size = int(t.numinput("Size", "Enter size: 10-100", 10, minval=1, maxval=100)),
#         radius= t.numinput("Radius", "Enter radius: 0.3-1", 0.3, minval=0.3, maxval=5),
#         radius_start=0
#         ):
#     """
#     :return: draw spiral
#     """
#     for _ in range(size):
#         for _ in range(30):
#             t.forward(radius_start)
#             t.left(6)
#         radius_start += radius

# def spiral_square(start_size=0,
#                   size=int(t.numinput("Size", "Enter size: 1-50", 1, minval=1, maxval=50)),
#                   count=int(t.numinput("Count square", "Enter count: 1-100", 1, minval=1, maxval=100)),
#                   ):
#     """
#     :return: draw spiral square
#     """
#     for _ in range(count * 4 + 1):
#         t.fd(start_size)
#         t.lt(90)
#         start_size += size

# def polygon(count):
#     """
#     :return: Draw many regular polygon.
#     """
#     while count <= n:
#         t.lt((180 - 360 / n) / 2)
#         t.lt(360 / n)
#         t.fd(2 * R * math.sin(math.pi/n))
#         count += 1
#         t.rt((180 - 360 / n) / 2)

# def flower(x=1,
#            n=t.numinput("Petals", "Enter count petals: 2-100", 6, minval=6, maxval=100),
#            r=t.numinput("Radius", "Enter radius: 10-100", 10, minval=2, maxval=100),
#            ):
#     """
#     :return: Draw circle in the form of flower
#     """
#     t.speed(10)
#     while x <= n:
#         t.circle(r)
#         t.left(360 / n)
#         x += 1

# def butterfly(radius=t.numinput("Radius", "Enter radius of wings: 10-50", 10, minval=10, maxval=50),
#            count=int(t.numinput("Count wings", "Enter count of wings: 1-20", 1, minval=1, maxval=20))
#            ):
#     """
#     :return: Draw buterfly
#     """
#     for _ in range(count):
#         t.seth(90)
#         t.circle(radius, 360)
#         t.circle(-radius, 360)
#         radius += 5

# def spring(count=int(t.numinput("Count round", "Enter count round in spring: 1-8 ", 1, minval=1, maxval=8)),
#            radius=t.numinput("Count Radius", "Enter radius spring: 40-80 ", 40, minval=40, maxval=80)
#            ):
#     """
#     Create Spring
#     :return: Draw spring.
#     """
#     t.left(90)
#     x = 1
#     while x <= count:
#         t.circle(-radius, 180)
#         t.circle(-10, 180)
#         x += 1

# def smile():
#     """
#     :return: Draw smile.
#     """
#     t.color('black')
#     t.up()
#     t.goto(100, 0)
#     t.left(90)
#     t.down()
#     t.fillcolor('yellow')
#     t.begin_fill()
#     t.circle(100)
#     t.end_fill()
#     t.up()
#     t.goto(-30, 50)
#     t.down()
#     t.fillcolor('blue')
#     t.begin_fill()
#     t.circle(15)
#     t.end_fill()
#     t.up()
#     t.goto(60, 50)
#     t.down()
#     t.fillcolor('blue')
#     t.begin_fill()
#     t.circle(15)
#     t.end_fill()
#     t.up()
#     t.goto(0, 30)
#     t.down()
#     t.color('black')
#     t.pensize(8)
#     t.left(180)
#     t.forward(50)
#     t.up()
#     t.goto(70, -10)
#     t.color('red')
#     t.down()
#     t.circle(-70, 180, 30)

# def stars(number_vertices=int(t.numinput("Vertices", "Enter number of vertices: 4-21 ", 5, minval=5, maxval=21))):
#     '''
#     :return: Draw Star with enter number of vertices.
#     '''
#     for _ in range(number_vertices):
#         t.left(180 - 180/number_vertices)
#         t.forward(200)


t.shape('turtle')
t.speed(10)


# Exercise 1: S
# symbolS()

# Exercise 2: Square
# square(int(t.numinput("Size square", "Distance between the squares 10-100", 10, minval=10, maxval=100)))

# Exercise 3: Circle
# circle()
# Or use the built-in turtle circle function

# Exercise 4: Nested square
# size = int(t.numinput("Size square", "Distance between the squares 10-50", 10, minval=10, maxval=50))
# x = size
# y = -(x/2)
# for _ in range(int(t.numinput("Count square", "Enter count square 1-20", 1, minval=1, maxval=20))):
#     square(x)
#     t.penup()
#     t.setpos(y, y)
#     t.pendown()
#     x += size
#     y = -(abs(y) + size/2)

# Exercise 5: Spider
# spider()

# Exercise 6: Spiral
# spiral()

# Exercise 7: Square spiral
# spiral_square()

# Exercise 8: Regular polygon
# quantity = int(t.numinput("Введите данные","Введите количество многоугольников: ", 1, minval=1, maxval=100))
# R = 30
# n = 3
# t.up()
# t.goto(R, 0)
# t.down()
# for i in range(quantity):
#     while n <= quantity + 2:
#         polygon(1)
#         n += 1
#         R += 18
#         t.up()
#         t.goto(R, 0)
#         t.down()

# Exercise 9: Flower
# flower()

# Exercise 10: Butterfly
# butterfly()

# Exercise 11: Spring
# spring()

# Exercise 12: Smile
# smile()

# Exercise 13:
# stars()
t.exitonclick()
