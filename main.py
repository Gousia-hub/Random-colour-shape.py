from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.pensize(2)

#list of colours to generate random colors
colours = ["hot pink", "violet", "dark orange", "deep sky blue", "pale green", "red", "medium purple", "medium blue",
           "chartreuse", "sandy brown", "rosy brown", "maroon", "aquamarine", "light sky blue", "medium violet red",
           "yellow", "spring green", "snow", "forest green", "midnight blue", "orange", "black", "pink", "dark orchid",
           "indian red"]

##OR
#a user_defined function which creates random colors from the color palette using RGB(Red Green Blue) standard colors ,which returns a tuple
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = (r,g,b)
    return  tup


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(0, num_sides):
        tim.forward(100)
        tim.left(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)



screen = Screen()
screen.exitonclick()
