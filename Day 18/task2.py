import turtle as T
import random

timmy = T.Turtle()
T.colormode(255)

def random_color():
   r = random.randint(0,255)
   g = random.randint(0,255)
   b = random.randint(0, 255)
   color = (r, g, b)
   return color


# Task 2: Draw Different shapes
timmy.pensize(3)
timmy.speed("slowest")
def draw(sides):
   angle = 360 / sides
   for _ in range(sides):
      timmy.forward(100)
      timmy.right(angle)

for n in range(3, 11):
   timmy.color(random_color())
   draw(n)

screen = T.Screen()
screen.exitonclick()

  