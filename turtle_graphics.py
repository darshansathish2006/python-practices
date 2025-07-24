# 1. Draw Square
'''
import turtle
skk = turtle.Turtle()

for i in range(4):
    skk.forward(50)
    skk.right(90)

turtle.done()
'''
# 2. Draw Star
# import turtle
# star = turtle.Turtle()

# star.right(75)
# star.forward(100)

# for i in range(4):
#     star.right(144)
#     star.forward(100)

# turtle.done()


# 3. Draw Hexagon

# import turtle
# polygon = turtle.Turtle()
# num_sides = 6
# side_length = 70
# angle = 360 / num_sides

# for i in range(num_sides):
#     polygon.forward(side_length)
#     polygon.right(angle)

# turtle.done()


# 4. Draw Parallelogram

# import turtle
# t = turtle.Turtle()
# t.speed(1)

# for i in range(2):
#     t.forward(100)
#     t.left(60)
#     t.forward(50)
#     t.left(120)

# turtle.done()


# 5. Draw Filled Circle

# import turtle
# screen = turtle.Screen()
# screen.bgcolor("green")
# pen = turtle.Turtle()
# pen.speed(10)

# pen.fillcolor("red")
# pen.begin_fill()
# pen.circle(200)
# pen.end_fill()
# pen.hideturtle()

# turtle.done()


# 6. Spiral Square Outside In and Inside Out

# import turtle

# def sqrfunc(size):
#     for i in range(4):
#         skk.forward(size)
#         skk.left(90)

# wn = turtle.Screen()
# wn.bgcolor("light green")
# skk = turtle.Turtle()
# skk.color("blue")

# size = 6
# for i in range(20):
#     sqrfunc(size)
#     size = size + 5

# turtle.done()


# 7. Spiral Helix Pattern

# import turtle
# loadWindow = turtle.Screen()
# turtle.speed(1)

# for i in range(100):
#     turtle.circle(5 * i)
#     turtle.circle(-5 * i)
#     turtle.left(i)

# turtle.exitonclick()


# 8. Rainbow Benzene Pattern
import turtle

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
t.speed(2)
screen=turtle.Screen()
screen.bgcolor('black')

for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x // 100 + 1)
    t.forward(x)
    t.left(59)

turtle.done()
