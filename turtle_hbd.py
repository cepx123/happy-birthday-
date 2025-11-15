import turtle as trtl
import math
import random

def ellipse_x(width, angle_deg):
    return width * math.cos(math.radians(angle_deg))

def ellipse_y(height, angle_deg):
    return height * math.sin(math.radians(angle_deg))

screen = trtl.Screen()
screen.bgcolor("#d3dae8")
screen.setup(900, 800)
screen.title("Happy Birthday Furina")

pen = trtl.Turtle()
pen.pensize(3)
pen.speed(0)
pen.hideturtle()

# Contoh sederhana: tulis "Happy Birthday"
pen.penup()
pen.goto(0,0)
pen.write("Happy Birthday!", align="center", font=("Curlz MT", 50, "bold"))

trtl.done()