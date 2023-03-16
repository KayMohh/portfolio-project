from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape("turtle")
timmy.color("Blue")
myscreen = Screen()
timmy.penup()
timmy.goto(-10, 270)
timmy.pendown()
# print(myscreen.canvheight)

num_sides = 4

def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(50)
        timmy.right(angle)
for shapes in range(3, 100):
    draw_shapes(shapes)
myscreen.exitonclick()

    # timmy.forward(100)
    # timmy.right(90)
    # timmy.forward(100)
    # timmy.right(90)
    # timmy.forward(100)
    # timmy.right(90)
    # timmy.forward(100)
    # print(timmy)

# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
# def solid_line():
#     for _ in range(10):
#         timmy.forward(100)
#
# def spaced_line():
#     for _ in range(10):
#         timmy.penup()
#         timmy.forward(15)
#         timmy.forward(5)
#         #timmy.pendown()
#
#
# def dashed_line():
#     for _ in range(10):
#         timmy.forward(15)
#         timmy.penup()
#         timmy.forward(5)
#         timmy.pendown()
# solid_line()
# dashed_line()
# spaced_line()
