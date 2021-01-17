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


# Task 3: Draw a random walk
directions = [0, 90, 180, 270]
timmy.pensize(14)

for _ in range(200):
   timmy.color(random_color())
   timmy.forward(30)
   timmy.setheading(random.choice(directions))

screen = T.Screen()
screen.exitonclick()

  