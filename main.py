import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def named_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.color(r, g, b)

def draw_circle(num_of_circles):
    angles = int(360/num_of_circles)
    tim.speed(0)
    for num in range(num_of_circles):
        named_color()
        tim.setheading(angles*num)
        tim.circle(50)

########### Challenge 4 - SpiroCircle ########

number_of_angles = int(input("how many circles do you want"))
draw_circle(number_of_angles)

s = t.Screen()
s.exitonclick()
